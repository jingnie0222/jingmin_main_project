"""main_project URL Configuration

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
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve
from html_test.views import R_test
from sra.views import sra
from user_record.views import login, logout

# from editor_md.views import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('R_test/', R_test),
    path('vr_query/', include('vr_query.urls')),
    path('front_press/', include('front_press.urls')),
    path('lizhi_accu_compare/', include('lizhi_accu_compare.urls', namespace='lizhi_accu_compare')),
    path('hx_inner_wiki/', include('hx_inner_wiki.urls')),
    path('editor_md/', include('editor_md.urls')),
    # path('upload/image', upload_image, name='editor_upload_image'),
    path('/static/media/<str:path>', serve, {"document_root": settings.MEDIA_ROOT}),
    path('sra/', sra),  # some static data shows. documents & entrys for frontweb.
    path('CodeTrigger/', include('CodeTrigger.urls')),
    path('autoFront/', include('autoFront.urls')),
    path('Minimum_Test_Set/', include('Minimum_Test_Set.urls')),
    path('OfflineFront/', include('OfflineFront.urls')),
    path('monitor_notice/', include('monitor_notice.urls')),
    path('front_vr_check_unit/', include('front_vr_check_unit.urls')),
]
