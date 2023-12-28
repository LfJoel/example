"""String_Similarity_Search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from String_Similarity_Search import settings
from Users import views as user_view

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$',user_view.user_login,name="user_login"),
    url(r'^base',user_view.base,name="base"),
    url(r'^user_register/$',user_view.user_register,name="user_register"),
    url(r'^user_home/$',user_view.user_home,name="user_home"),
    url(r'^remove-document/(?P<did>\d+)/$', user_view.remove, name='remove'),
    url(r'^user_upload/$',user_view.user_upload,name="user_upload"),
    url(r'^analysis-list/$', user_view.docanalysis, name='analysislist'),
    url(r'^analysis/(?P<did>\d+)/$',user_view.analysissingle, name='analysisdoc'),
    url('analysis_chart/(?P<chart_type>\w+)', user_view.analysis_chart, name="analysis_chart"),
    url(r'^ucharts/(?P<chart_type>\w+)', user_view.ucharts,name="ucharts"),
    url(r'^user_match/$',user_view.user_match,name="user_match"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
