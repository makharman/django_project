
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

# from post.views import page_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('account/', include('account.urls')),
    # path('api/v2'),
]

# handler404 = page_404

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)