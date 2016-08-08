# coding=utf-8
from datetime import datetime

from django.db import models
from django.db.models import Manager
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


class Images(models.Model):
    image = models.ImageField(upload_to='pics')

    def __unicode__(self):
        return str(self.id)


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', )
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Родительская категория')
    slug = models.SlugField(unique=True, verbose_name='Краткое название')
    default_image = models.ForeignKey(Images, blank=True, null=True, verbose_name='Изображение')

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)

    def clean(self):
        if self.id and self.id == self.parent_id:
            raise ValidationError("Category id can't equals category parent id")
        if self.get_level() > 3:
            raise ValidationError('Max level for subcategories is 3')
        if not self.parent and not self.default_image:
            raise ValidationError('Root catalog must have image')

    def get_image(self):
        if not self.default_image:
            category = self.parent
            while not category.default_image:
                category = category.parent
            return category.default_image
        return self.default_image

    def get_absolute_url(self):
        url = '/'
        current_category = self
        while current_category:
            if current_category.slug:
                url = '/%s%s' % (current_category.slug, url)
                current_category = current_category.parent
        return url

    def get_level(self):
        level = 0
        category = self
        while category:
            level += 1
            category = category.parent
        return level

    def get_breadcrumbs(self):
        breadcrumbs = []
        category = self
        while category:
            breadcrumbs = [(category.name, category.get_absolute_url(), category.slug)] + breadcrumbs
            category = category.parent
        return breadcrumbs


class ReleasedProductManager(Manager):
    def get_query_set(self):
        return super(ReleasedProductManager, self).get_query_set().filter(release_date__lt=datetime.now())

    def for_user(self, user):
        return self.all() if user.is_authenticated() else self.exclude(is_hidden=True)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Categories, verbose_name='Категория')
    count = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    release_date = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name='Начало продаж')
    is_hidden = models.BooleanField(default=False, verbose_name='Cкрыть на сайте')
    image = models.ForeignKey(Images, blank=True, null=True, verbose_name='Изображение')

    objects = models.Manager()
    released = ReleasedProductManager()

    def __unicode__(self):
        return "%s - %s" % (self.id, self.name)

    def get_image(self):
        if not self.image:
            return self.category.get_image()
        return self.image

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id])
