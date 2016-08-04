# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


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

    def clean(self):
        if self.id == self.parent_id:
            raise ValidationError("Category id can't equals category parent id")
        if self.get_level() > 3:
            raise ValidationError('Max level for subcategories is 3')
        if not self.parent and not self.default_image:
            raise ValidationError('Root catalog must have image')

    def get_absolute_url(self):
        url = '/'
        current_category = self
        while current_category:
            if current_category.slug:
                url = '/%s%s' % (current_category.slug, url)
                current_category = current_category.parent
        return url

    def get_level(self):
        return len(self.get_breadcrumbs())

    def get_breadcrumbs(self):
        breadcrumbs = []
        category = self
        while category:
            breadcrumbs = [(category.name, category.get_absolute_url(), category.slug)] + breadcrumbs
            category = category.parent
        return breadcrumbs

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories)
    count = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ForeignKey(Images, blank=True, null=True)

    def get_image(self):
        if not self.image:
            return self.category.get_image()
        return self.image

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse("testapp.views.product_details", args=[self.id])
