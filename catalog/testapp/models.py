# coding=utf-8

from django.db import models
from django.template.defaultfilters import slugify


class Images(models.Model):
    image = models.ImageField(upload_to='pics')

    def __unicode__(self):
        return str(self.id)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    default_image = models.ForeignKey(Images, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        old_category = Categories.objects.filter(id=self.id)
        if old_category:
            old_image = old_category[0].default_image
            child_ids = self.get_all_level_child_ids()
            Categories.objects.filter(id__in=child_ids, default_image=old_image).update(default_image=self.default_image)

        # try:
        #     old_category = Categories.objects.get(id=self.id)
        #     assert False, old_category.parent
        #     if old_category:
        #         child_ids = self.get_all_level_child_ids()
        #
        #         old_image = old_category.default_image
        #         if old_category.parent != self.parent:
        #             if self.parent:
        #                 image = self.parent.default_image
        #             else:
        #                 image = self.default_image
        #             Categories.objects.filter(id__in=child_ids).update(default_image=image)
        #         else:
        #             be_changes = Categories.objects.filter(id__in=child_ids, default_image=old_image)
        #             be_changes.update(default_image=self.default_image)
        # except Categories.DoesNotExist:
        #     pass


        if self.parent and not self.default_image:
            self.default_image = self.parent.default_image
        super(Categories, self).save(*args, **kwargs)

    # @models.permalink
    def get_absolute_url(self):
        current_category = self
        url = '/'
        while current_category:
            if current_category.slug:
                url = '/' + current_category.slug + url
                current_category = current_category.parent

        return url

    def get_level(self):
        return len(filter(bool, self.get_absolute_url().split('/')))

    def get_all_level_child_ids(self):
        ids = []
        childs = Categories.objects.filter(parent=self.id)
        # ids.append(self.id)
        for child in childs:
            ids.append(child.id)
            ids += child.get_all_level_child_ids()
        return ids

    def __unicode__(self):
        test_name = str(self.id) + ' | ' + self.name + ' | ' + self.slug + ' | '
        test_name += str(self.get_level()) + ' | ' + self.get_absolute_url()
        return test_name

    class Meta:
        unique_together = ("id", "default_image")


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, blank=True, null=True)
    count = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ForeignKey(Images, blank=True, null=True)

    def get_image(self):
        if not self.image:
            return self.category.default_image.image.url
        else:
            return self.image.image.url

    def __unicode__(self):
        return str(self.id) + ' | ' + self.name

    # @models.permalink
    def get_absolute_url(self):
        return "/product/" + str(self.id)
