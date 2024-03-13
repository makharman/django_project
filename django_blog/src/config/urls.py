
from django.contrib import admin
from django.urls import path,include

from post.views import page_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls'))
]

handler404 = page_404