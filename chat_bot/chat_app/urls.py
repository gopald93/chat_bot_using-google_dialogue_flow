from django.urls import path
from chat_app import  views 
urlpatterns = [
	path('activities_analysis/', views.activities_analysis, name='activities_analysis'),
	path('api_extraction/', views.api_extraction, name='api_extraction'),
	path('',  views.home_messages, name='home_messages'),
	path('owner_messages/', views.owner_messages, name='owner_messages'),
	path('webhook/', views.webhook, name='webhook'),
    path('post_request_data/',  views.post_request_data, name='post_request_data'),
    path('get_success_message_details/',  views.get_success_message_details, name='get_success_message_details'),
    path('get_failed_message_details/',  views.get_failed_message_details, name='get_failed_message_details'),
    path('show_all_messages/',  views.show_all_messages, name='show_all_messages'),
    
]

