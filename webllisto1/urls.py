from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from products.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',register,name='register'),
    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('products/',include('products.urls',namespace='products'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)