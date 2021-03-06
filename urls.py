# -*- coding: utf-8 -*-  

from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
from django.conf import settings
import os

from settings import DEBUG
import views

site_media = os.path.join(os.path.dirname(__file__), 'media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( 
    'views',
    # Example:
    (r'^wishes/(?P<status>\w+)?/?$', views.wishes),
    (r'^extsearch/', views.extsearch),
    (r'^logout/', 'logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^new/', 'new'),
    (r'^reserved', 'reservedwishes'),
    (r'^completed', 'completedwishes'),
    (r'^addstuff/', 'addstuff'),
    (r'^wish/(?P<userid>\d+)/$', 'userwish'),
    (r'^delete/(?P<num>\d+)/$', 'delete'),
    (r'^edit/(?P<num>\d+)/$', 'edit'),
    (r'^history/(?P<num>\d+)/$', 'showhistory'),
    (r'^status/(?P<st>\w+)/$', 'showstatus'),
    (r'^contact/', 'contact'),
    #(r'^todo/', include('todo.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #главная страница, авторизация, после нее показ 
    #всего остального или же отказ при неправильном пароле.
    #(r'^hello/$', 'hello'), 
    #или так:
    (r'^$', 'main'),    
    #(r'^$', direct_to_template, {'template':'base.html'}),                   
    #список наличного оборудования
    #(r'^available/$', show_avail),
    #список заказов                   
    #(r'^orders\$', show_orders),             
    #новый заказ
    #(r'^new_order\$'),
    )

if DEBUG:
    urlpatterns += patterns('', (
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': 'static'}
            ))
