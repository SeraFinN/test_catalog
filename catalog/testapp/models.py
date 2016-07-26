# coding=utf-8

from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from testapp.validators import SubCategoryURLValidator


class Images(models.Model):
    image = models.ImageField(upload_to='tmp')


class Categories(models.Model):
    name = models.CharField('Название', max_length=100)
    level = models.IntegerField(editable=False, validators=[MaxValueValidator(3)]) # validator don't work with calc field?
    parent = models.ForeignKey('self', blank=True, null=True,)
    fullUrl = models.CharField(editable=False, max_length=255)
    subCategoryUrl = models.CharField(max_length=20, validators=[SubCategoryURLValidator()])
    default_image = models.ForeignKey(Images, blank=True, null=True) # validator for control that root category have image

    def save(self, *args, **kwargs):
        self.subCategoryUrl = self.subCategoryUrl.lower()
        if self.parent:
            self.fullUrl = self.parent.fullUrl + self.subCategoryUrl + '/'
            self.default_image = self.parent.default_image
        else:
            self.fullUrl = '/' + self.subCategoryUrl + '/'
        self.level = len([subCategory for subCategory in self.fullUrl.split('/') if subCategory])
        if self.level > 3:
            raise ValidationError
        super(Categories, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name + ' | ' + self.fullUrl + ' | ' + str(self.level)


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



