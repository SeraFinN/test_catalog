# coding=utf-8
from django.db import models
from django.db.models import Manager
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.core.cache import cache
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, post_delete

from local_setting import CATEGORIES_CACHE_NAME


class Images(models.Model):
    image = models.ImageField(upload_to='pics', verbose_name='Изображение')

    def __unicode__(self):
        return "%s - %s" % (self.pk, self.image)


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', )
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Родительская категория')
    slug = models.SlugField(unique=True, verbose_name='Краткое название')
    default_image = models.ForeignKey(Images, blank=True, null=True, verbose_name='Изображение')

    def __unicode__(self):
        return "%s - %s" % (self.pk, self.name)

    def save(self, **kwargs):
        self.slug = slugify(self.slug)
        super(Categories, self).save(**kwargs)

    def clean(self):
        if self.pk and self.pk == self.parent_id:
            raise ValidationError('Category id can\'t equals category parent id')
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
            breadcrumbs = [{'name': category.name, 'url': category.get_absolute_url()}] + breadcrumbs
            category = category.parent
        return breadcrumbs


class ReleasedProductManager(Manager):
    def for_user(self, user):
        if not user.is_authenticated():
            return self.get_query_set().exclude(is_hidden=True)
        return self.get_query_set()


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Categories, verbose_name='Категория')
    count = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыть на сайте')
    image = models.ForeignKey(Images, blank=True, null=True, verbose_name='Изображение')

    objects = models.Manager()
    released = ReleasedProductManager()

    def __unicode__(self):
        return "%s - %s" % (self.pk, self.name)

    def get_image(self):
        if not self.image:
            return self.category.get_image()
        return self.image

    def get_absolute_url(self):
        return reverse("catalog.views.product_details", args=[self.id])


@receiver(post_save, sender=Categories)
@receiver(post_delete, sender=Categories)
def invalidate_cache(sender, **kwargs):
    cache.delete(CATEGORIES_CACHE_NAME)
