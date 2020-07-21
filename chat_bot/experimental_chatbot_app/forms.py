from django import forms
from django.forms import formset_factory
from chat_app.models import Statement,Message,Owner_Handling_Message
from experimental_chatbot_app.common import get_length_for_formset

list_of_question=get_length_for_formset()
class GeeksForm(forms.Form):
    title = forms.CharField(max_length = 200)
    description=forms.CharField(max_length = 200)

GeeksFormSet = formset_factory(GeeksForm,extra=0) 
