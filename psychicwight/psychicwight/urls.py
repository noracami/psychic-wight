from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psychicwight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'quiz.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quiz/', include('quiz.urls', namespace="quiz")),
)
