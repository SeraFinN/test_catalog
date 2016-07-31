# coding=utf-8

from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


class Images(models.Model):
    image = models.ImageField(upload_to='pics')

    def __unicode__(self):
        return str(self.id)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='category')
    slug = models.SlugField(unique=True, blank=True)
    default_image = models.ForeignKey(Images, blank=True, null=True)

    def get_image(self):
        if not self.default_image:
            category = self.parent
            while not category.default_image:
                category = category.parent
            return category.default_image
        return self.default_image

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    def clean(self):
        if not self.parent and not self.default_image:
            raise ValidationError('Root catalog must have image')

    def get_absolute_url(self):
        current_category = self
        url = '/'
        # bread = self.get_breadcrumbs()
        # for slug in bread:
        #     url = url + "/" + slug[2]
        # assert False, url
        # url = []
        while current_category:
            if current_category.slug:
                url = '/' + current_category.slug + url
                current_category = current_category.parent
        return url

    def get_level(self):
        return len(filter(bool, self.get_absolute_url().split('/')))

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
        test_name = str(self.id) + ' | ' + self.name + ' | '
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
        return "/product/" + str(self.id)
