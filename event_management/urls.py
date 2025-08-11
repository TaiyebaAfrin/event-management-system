
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from tasks import views 
from core.views import home, no_permission
#from django.views.generic import TemplateView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='events/home.html')),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    path('', home, name="home"),
    path('no-permission/', no_permission, name='no-permission')
]+ debug_toolbar_urls()
