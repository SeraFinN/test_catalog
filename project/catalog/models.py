# coding=utf-8
from django.db import models
from django.db.models import Manager
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify


class Images(models.Model):
    image = models.ImageField(upload_to='pics')

    def __unicode__(self):
        return str(self.pk)


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', )
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Родительская категория')
    slug = models.SlugField(unique=True, verbose_name='Краткое название')
    default_image = models.ForeignKey(Images, blank=True, null=True, verbose_name='Изображение')

    def __init__(self, *args, **kwargs):
        super(Categories, self).__init__(*args, **kwargs)
        self._parents = []
        self.count = 0
        self.count_base = 0
        self.count_url = 0
        self.count_level = 0
        self.count_bread = 0

    def __unicode__(self):
        return "%s - %s" % (self.pk, self.name)

    def save(self, **kwargs):
        self.slug = slugify(self.slug)
        super(Categories, self).save(**kwargs)

    def clean(self):
        if self.pk and self.pk == self.parent_id:
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

    def _get_all_parents(self):
        if self._parents:
            self.count += 1
            print "count %s %s" % (self.count, self.slug)
            return self._parents
        category = self
        while category:
            self._parents.append(category)
            category = category.parent
        self.count_base += 1
        print "count base %s %s" % (self.count_base, self.slug)
        return self._parents

    def get_absolute_url(self):
        self.count_url += 1
        print "count url %s" % self.count_url
        return '/%s/' % '/'.join(category.slug for category in reversed(self._get_all_parents()))

    def get_level(self):
        self.count_level += 1
        print "count level %s" % self.count_level
        return len(self._get_all_parents())

    def get_breadcrumbs(self):
        self.count_bread += 1
        print "count bread %s" % self.count_bread
        return [{'name': x.name, 'url': x.get_absolute_url()} for x in reversed(self._get_all_parents())]


class ReleasedProductManager(Manager):
    def get_query_set(self):
        return super(ReleasedProductManager, self).get_query_set().exclude(is_hidden=True)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Categories, verbose_name='Категория')
    count = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    is_hidden = models.BooleanField(default=False, verbose_name='Cкрыть на сайте')
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
        return reverse("product_detail", args=[self.id])
