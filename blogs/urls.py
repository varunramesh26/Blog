"""Defines URL patterns for blogs."""

from django.conf.urls import url

from . import views

urlpatterns = [
        # Home page
        url(r'^$', views.index, name='index'),

        # Show all blogposts
        url(r'^blogposts/$', views.blogposts, name='blogposts'),

        # Show a particular blogpost.
        url(r'^blogposts/(?P<blogpost_id>\d+)/$', views.blogpost, name='blogpost'),

        # Page for adding a new Blogpost.
        url(r'^new_blogpost/$', views.new_blogpost, name='new_blogpost'),

        # Page for adding a new blogpost content.
        url(r'^new_entry/(?P<blogpost_id>\d+)/$', views.new_entry, name='new_entry'),

        # Page for editing a blogpost content.
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

