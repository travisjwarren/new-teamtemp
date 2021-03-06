from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from teamtemp.views import home, admin, submit, reset, bvc, team, cron, set, _bvc

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^cs$', home, {'survey_type' : 'CUSTOMERFEEDBACK'}),
    url(r'^about$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})$', admin),
    url(r'^set/(?P<survey_id>[0-9a-zA-Z]{8})$', set),
    url(r'^admin/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>\w{1,64})$', admin),
    url(r'^(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>\w{1,64})$', submit),
    url(r'^_bvc/(?P<survey_id>[0-9a-zA-Z]{8})$', _bvc),
    url(r'^_bvc/(?P<survey_id>[0-9a-zA-Z]{8})/', include([
                                                          url(r'(?P<archive_id>[0-9]{1,20})$', _bvc),
                                                          url(r'(?P<team_name>\w{1,64})/i(?P<num_iterations>[0-9]{1,3})$', _bvc),
                                                          url(r'(?P<team_name>\w{1,64})$', _bvc),
                                                          url(r'(?P<team_name>\w{1,64})/(?P<archive_id>[0-9]{1,20})$', _bvc),
                                                          url(r'i(?P<num_iterations>[0-9]{1,3})$', _bvc),
                                                          ])),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})$', bvc),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/i(?P<num_iterations>[0-9]{1,3})$', bvc),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>\w{1,64})/i(?P<num_iterations>[0-9]{1,3})$', bvc),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<archive_id>[0-9]{1,20})$', bvc),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>\w{1,64})$', bvc),
    url(r'^bvc/(?P<survey_id>[0-9a-zA-Z]{8})/(?P<team_name>\w{1,64})/(?P<archive_id>[0-9]{1,20})$', bvc),
    url(r'^reset/(?P<survey_id>[0-9a-zA-Z]{8})$', reset),
    url(r'^cron/(?P<pin>[0-9]{4})$', cron),
    url(r'^team/(?P<survey_id>[0-9a-zA-Z]{8})$', team),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
