from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home, greetings, now, favicon

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('greetings/', greetings, name='greetings'),
    path('now/', now, name='now'),
    path('favicon.ico', favicon, name='favicon'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
