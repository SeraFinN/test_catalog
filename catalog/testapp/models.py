# coding=utf-8

from django.db import models

from django.template.defaultfilters import slugify


class Images(models.Model):
    image = models.ImageField(upload_to='pics')


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    default_image = models.ForeignKey(Images, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.parent:
            self.default_image = self.parent.default_image
        super(Categories, self).save(*args, **kwargs)

    # @models.permalink
    def get_absolute_url(self):
        current_category = self
        url = '/'
        while current_category:
            if current_category.slug:
                url = '/' + current_category.slug + url
                #url.append(str(current_category.slug))
                current_category = current_category.parent

        return url

    def get_level(self):
        return len(filter(bool, self.get_absolute_url().split('/')))

    def __unicode__(self):
        return str(self.id) + ' | ' + self.name + ' | ' + self.slug + ' | ' + str(self.get_level()) + ' | ' + self.get_absolute_url()


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, blank=True, null=True)
    count = models.IntegerField()
    price = models.IntegerField()
    image = models.ForeignKey(Images, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = self.category.default_image
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
