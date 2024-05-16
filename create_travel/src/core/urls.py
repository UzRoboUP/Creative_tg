from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from .yasg import schema_view



urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include("app.urls")),
    path('', include("press_service.urls")),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  
]

# urlpatterns += i18n_patterns(
#     path('', include("app.urls")),
#  )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    