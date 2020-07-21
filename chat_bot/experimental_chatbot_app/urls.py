from django.urls import path
from . import views
urlpatterns = [
	path('formset_view/', views.formset_view, name='formset_view'),
	path('templates_prepare/', views.templates_prepare, name='templates_prepare'),
	path('second_index_page/', views.second_index_page, name='second_index_page'),
]