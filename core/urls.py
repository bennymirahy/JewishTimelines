from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),
    url(r'^api/events/save$', views.save_event),
    url(r'^api/events$', views.list_event),
    url(r'^api/events/(?P<pk>\d+)/remove$', views.remove_event),
    url(r'^api/events/(?P<pk>\d+)$', views.get_event)


]
