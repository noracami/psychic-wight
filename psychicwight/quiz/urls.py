from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psychicwight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'quiz.views.home', name='home'),
    #url(r'^quiz/$', 'quiz.views.search', name='search'),

    # ... the rest of your URLconf goes here ...
)
