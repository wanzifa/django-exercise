from django.test import TestCase
from models import Category
from django.core.urlresolvers import reverse
from rango.models import Category, Page

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')


class IndexViewsTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
class IndexViewsTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp', 1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test tmp")

        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)

class TestPageMethod(TestCase):
    def test_ensure_first_and_last_visit(self):
        cat = Category(name='test', views=1, likes=0)
        cat.save()
        p = Page(title='xixi',category=cat)
        p.save()
        #response = self.client.get(reverse('add_page',kwargs={'catgory_slug_name':cat.slug}))
        response = self.client.get(reverse('goto'))
        first_visit = p.first_visit
        last_visit = p.last_visit
        self.assertEqual((first_visit < last_visit), True)
