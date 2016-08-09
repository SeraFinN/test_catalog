# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.management import call_command

from catalog.models import Categories
from catalog.formater import get_categories_list, prepare_data
from catalog.views import product_list


class SimpleTest(TestCase):
    def setUp(self):
        mon = Categories.objects.create(name=u'Мониторы', parent=None, slug='monitors')
        Categories.objects.create(name='19', parent=mon, slug='19')
        Categories.objects.create(name='21', parent=mon, slug='21')
        cpu = Categories.objects.create(name=u'Процессоры', parent=None, slug='cpu')
        intel = Categories.objects.create(name='intel', parent=cpu, slug='intel')
        amd = Categories.objects.create(name='amd', parent=cpu, slug='amd')
        Categories.objects.create(name='intel-notebook', parent=intel, slug='intel-notebook')
        Categories.objects.create(name='amd-notebook', parent=amd, slug='amd-notebook')
        Categories.objects.create(name=u'Видео-карты', parent=None, slug='video-carts')
        # assert False, Categories.objects.all()

    def load_fixture(self):
        call_command('loaddata', '/home/serafinn/develop/djangoCatalog/project/fixtures.json', commit=False, verbosity=0)

    def test_num_queries_fast(self):
        # self.setUp()
        # assert False, len(Categories.objects.all())
        self.load_fixture()
        with self.assertNumQueries(0):
            cat = Categories.objects.select_related('parent').get(id=7)
            cur = cat
            while cur:
                cur = cur.parent
            # list(Categories.objects.all())

    def test_num_queries_main(self):
        self.load_fixture()

        self.assertNumQueries(0, func=get_categories_list)

    def test_num_queries_old(self):
        self.load_fixture()
        self.assertNumQueries(0, func=prepare_data)
