from django.shortcuts import render
from .forms import GeeksForm,GeeksFormSet
from django.http import HttpResponse
from chat_app.models import Statement,Message,Owner_Handling_Message
from experimental_chatbot_app.common import get_length_for_formset

def templates_prepare(request):
    return render(request, "experimental_chatbot_app/krishna.html")

def second_index_page(request):
    return render(request, "experimental_chatbot_app/second_index_page.html")
    
def formset_view(request): 
    context ={} 
    if request.method=="POST":
        formset = GeeksFormSet(request.POST or None) 
        if formset.is_valid(): 
            for form in formset: 
                print(form.cleaned_data) 
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        list_of_question=get_length_for_formset()
        check_demo_list=[]
        for question in list_of_question:
            check_demo_list.append({'title':question})
        formset_demo= GeeksFormSet(initial=check_demo_list)
        context['formset']=formset_demo
        return render(request, "experimental_chatbot_app/home.html", context)
