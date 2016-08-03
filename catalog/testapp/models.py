# coding=utf-8

from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse


class Images(models.Model):
    image = models.ImageField(upload_to='pics')

    def __unicode__(self):
        return str(self.id)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.SlugField(unique=True)
    default_image = models.ForeignKey(Images, blank=True, null=True)

    def get_image(self):
        if not self.default_image:
            category = self.parent
            while not category.default_image:
                category = category.parent
            return category.default_image
        return self.default_image

    def save(self, *args, **kwargs):
        if self.id == self.parent_id:
            raise ValidationError("Category id can't equals category parent id")
        if self.get_level() > 3:
            raise ValidationError('Max level for subcategories is 3')
        if not self.parent and not self.default_image:
            raise ValidationError('Root catalog must have image')
        super(Categories, self).save(*args, **kwargs)

    # def clean(self):
    #     if self.id == self.parent_id:
    #         raise ValidationError("Category id can't equals category parent id")
    #     if self.get_level() > 3:
    #         raise ValidationError('Max level for subcategories is 3')
    #     if not self.parent and not self.default_image:
    #         raise ValidationError('Root catalog must have image')

    def get_absolute_url(self):
        current_category = self
        url = '/'
        while current_category:
            if current_category.slug:
                url = '/' + current_category.slug + url
                current_category = current_category.parent
        return url

    def get_level(self):
        return len(self.get_breadcrumbs())

    def get_breadcrumbs(self):
        breadcrumbs = []
        current_category = self
        while current_category:
            if current_category.slug:
                breadcrumbs_tuple = (current_category.name, current_category.get_absolute_url(), current_category.slug)
                breadcrumbs = [breadcrumbs_tuple] + breadcrumbs
                current_category = current_category.parent
        return breadcrumbs

    def __unicode__(self):
        test_name = str(self.id) + ' | ' + self.name + ' | ' + str(self.get_level())
        # test_name += str(self.get_level()) + ' | ' + self.get_absolute_url()
        return test_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, blank=True, null=True)
    count = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ForeignKey(Images, blank=True, null=True)

    def get_image(self):
        if not self.image:
            return self.category.get_image()
        return self.image

    def __unicode__(self):
        return str(self.id) + ' | ' + self.name

    def get_absolute_url(self):
        return reverse("product_details", args=[self.id])
