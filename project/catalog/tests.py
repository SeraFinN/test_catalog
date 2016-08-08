# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from catalog.models import Categories
from catalog.formater import get_categories_list, prepare_data


class SimpleTest(TestCase):
    def set_up(self):
        mon = Categories.objects.create(name=u'Мониторы', parent=None, slug='monitors')
        Categories.objects.create(name='19', parent=mon, slug='19')
        Categories.objects.create(name='21', parent=mon, slug='21')
        cpu = Categories.objects.create(name=u'Процессоры', parent=None, slug='cpu')
        intel = Categories.objects.create(name='intel', parent=cpu, slug='intel')
        amd = Categories.objects.create(name='amd', parent=cpu, slug='and')
        Categories.objects.create(name='intel-notebook', parent=intel, slug='intel-notebook')
        Categories.objects.create(name='amd-notebook', parent=amd, slug='amd-notebook')
        Categories.objects.create(name=u'Видео-карты', parent=None, slug='video-carts')

    def test_num_queries_main(self):
        self.set_up()
        self.assertNumQueries(0, func=get_categories_list)

    def test_num_queries_old(self):
        self.set_up()
        self.assertNumQueries(1, func=prepare_data)
