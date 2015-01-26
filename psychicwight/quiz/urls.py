from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psychicwight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'quiz.views.home', name='home'),
    url(r'(?P<section>random)/$', 'quiz.views.maintenanceknowledge', name='maintenanceknowledge'),
    url(r'(?P<section>random)/(?P<showall>a)/$', 'quiz.views.maintenanceknowledge', name='maintenanceknowledge'),
    url(r'(?P<section>\D+)/(?P<number>\d+)/$', 'quiz.views.maintenanceknowledge', name='maintenanceknowledge'),
    url(r'(?P<section>\D+)/(?P<number>\d+)/(?P<showall>a)/$', 'quiz.views.maintenanceknowledge', name='maintenanceknowledge'),
    #url(r'^quiz/$', 'quiz.views.search', name='search'),

    # ... the rest of your URLconf goes here ...
)
