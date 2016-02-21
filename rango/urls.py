from django.conf.urls import url
from rango import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r"^about", views.about, name='about'),
        url(r"^add_category/$", views.add_category, name="add_category"),
        url(r"^category/(?P<category_name_slug>[\w\-]+)$", views.category, name='category'),
        url(r"^page/(?P<page_name_slug>[\w\-]+)$", views.page, name='page'),
        url(r'^add_page/(?P<category_name_slug>[\w\-]+)$', views.add_page, name='add_page'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^register/$', views.register, name='register'),
        url(r'^logout/$', views.user_logout, name='logout'),
]
