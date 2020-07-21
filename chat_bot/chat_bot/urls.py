from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('chat_app/', include('chat_app.urls')),
	path('experimental_chatbot_app/', include('experimental_chatbot_app.urls')),
    path('admin/', admin.site.urls),
]

