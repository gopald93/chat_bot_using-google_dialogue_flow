from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import dialogflow
import os
from .models import Statement,Message,Owner_Handling_Message
from chat_bot.library.df_response_lib import *
import collections    
from datetime import datetime
import operator 
import requests

def api_extraction(request):
    print("==================================>")
    response = requests.get('http://activitytracing.pythonanywhere.com/activity_periods_api/')
    print(response)
    geodata = response.json()
    return HttpResponse("Hello, world. You're at the polls index.")


def home_messages(request):
    return render(request, "chat_app/message.html")

def show_all_messages(request):
    context={}
    message_obj=Message.objects.all().order_by('-created_date')
    context["message"]=message_obj
    return render(request, "chat_app/show_all_messages.html",context)

def get_success_message_details(request):
    context={}
    message_obj=Message.objects.filter(reply_status=True)
    context["message"]=message_obj
    return render(request, "chat_app/success_message_details.html",context)

def get_failed_message_details(request):
    context={}
    message_obj=Message.objects.filter(reply_status=False)
    context["message"]=message_obj
    return render(request, "chat_app/failed_message_details.html",context)

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)
    return data
    
@csrf_exempt
@require_http_methods(['POST'])
def post_request_data(request):
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['name']
    GOOGLE_AUTHENTICATION_FILE_NAME = "krishna-demo-hfllhb-551060e45410.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
    GOOGLE_PROJECT_ID = "krishna-demo-hfllhb"
    session_id = "1234567891"
    context_short_name = "does_not_matter"
    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + \
               context_short_name.lower()
    parameters = dialogflow.types.struct_pb2.Struct()
    context_1 = dialogflow.types.context_pb2.Context(
        name=context_name,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        lifespan_count=2,
        parameters=parameters
    )
    query_params_1 = {"contexts": [context_1]}
    language_code = 'en'
    response = detect_intent_with_parameters(
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        query_params=query_params_1,
        language_code=language_code,
        user_input=input_text
    )
    print("response===================>")
    print(response)
    print("response===================>")
    reach_messages_data=None

    if operator.contains(str(response),"link_out_suggestion"): 
        humans_clickable_bot_link=None
        for data in response.query_result.fulfillment_messages:
            if data.link_out_suggestion.uri: 
                humans_clickable_bot_link='''<a class="btn btn-primary" href="%s"  target="_blank" role="button">click here</a>'''%(data.link_out_suggestion.uri)
        reach_messages_data=humans_clickable_bot_link
    
    if operator.contains(str(response),"suggestions"): 
        suggestions_list=[]
        temp=1
        for data in response.query_result.fulfillment_messages:
            if len(data.suggestions.suggestions)>0:
                for demo_data in data.suggestions.suggestions:
                    demo_data_button='''<button type="button" class="button button5" id=%s onclick="callbuttonfunction(%s)"> %s </button>'''%(str(temp),str(temp),demo_data.title)
                    temp=temp+1
                    suggestions_list.append(demo_data_button)     
        button_screen='  '
        button_screen=button_screen.join(suggestions_list)
        reach_messages_data=button_screen                       
    
    data_creation_obj=None
    statement_obj = Statement.objects.create(text=input_text)
    if response.query_result.intent.display_name=="Default Fallback Intent":
        data_creation_obj=Message.objects.create(statement=statement_obj,response=response.query_result.fulfillment_text,intent=response.query_result.intent.display_name,reply_status=False)
        owner_handling_message_obj=Owner_Handling_Message.objects.create(statement=statement_obj)  
    else:
        data_creation_obj=Message.objects.create(statement=statement_obj,response=response.query_result.fulfillment_text,intent=response.query_result.intent.display_name,reply_status=True)
    message = {'id':data_creation_obj.id,'statement':data_creation_obj.statement.text,'response':data_creation_obj.response,"reply_status":data_creation_obj.reply_status}

    data = {
        'reach_messages_data':reach_messages_data,
        'message': message}
    return JsonResponse(data,status=200)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def detect_intent_with_parameters(project_id, session_id, query_params, language_code, user_input):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text = user_input
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input,
        query_params=query_params
    )
    return response

def owner_messages(request):
    owner_handling_message_obj= Owner_Handling_Message.objects.order_by('created_date')
    print("owner_handling_message_obj===>",owner_handling_message_obj)
    return render(request, "chat_app/owner_messages.html",{"owner_handling_message_obj":owner_handling_message_obj})

@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    action = req.get('queryResult').get('action')
    print("action=====>",action)
    fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    print("fulfillmentText====>",fulfillmentText)
    return JsonResponse(fulfillmentText, safe=False)

def activities_analysis(request):
    total_obj=Message.objects.all()
    count=0
    total_count_list=[['CREATED_DATETIME','COUNT']]
    for field in total_obj:
        if field.reply_status==True:
            count=count+1
        if field.reply_status==False:
            count=count-1

        created_date=(field.created_date).strftime("(%Y,%m,%d,%H)")
        total_count=count
        total_count_list.append([created_date,total_count])
    total_count_list_json=json.dumps(total_count_list)

    total_messages=Message.objects.all().count()
    total_messages_json=json.dumps(total_messages)

    total_true_messages=Message.objects.filter(reply_status=True).count()
    total_true_messages_json=json.dumps(total_true_messages)

    total_failed_messages=Message.objects.filter(reply_status=False).count()
    total_failed_messages_json=json.dumps(total_failed_messages)

    if request.method=='POST':
        # ALL COUNT GRAPH
        from_date=request.POST.get('from_date')
        f_date=tuple(from_date.split()[0].split('/'))
        f_time=tuple(from_date.split()[1].split(':'))
        from_datetime_str=f_date+f_time
        from_date_converted=datetime(int(from_datetime_str[2]),int(from_datetime_str[0]),int(from_datetime_str[1]),int(from_datetime_str[3]),int(from_datetime_str[4]))


        to_date=request.POST.get('to_date')
        t_date=tuple(to_date.split()[0].split('/'))
        t_time=tuple(to_date.split()[1].split(':'))
        to_datetime_str=t_date+t_time
        to_date_converted=datetime(int(to_datetime_str[2]),int(to_datetime_str[0]),int(to_datetime_str[1]),int(to_datetime_str[3]),int(to_datetime_str[4]))

        #TOTAL COUNT GRAPH

        total_obj=Message.objects.filter(created_date__range=(from_date_converted,to_date_converted))

        count=0
        total_count_list=[['CREATED_DATETIME','TOTAL_COUNT']]
        for field in total_obj:
            if field.reply_status==True:
                count=count+1
            if field.reply_status==False:
                count=count-1

            created_date=(field.created_date).strftime("(%Y,%m,%d,%H)")
            total_count=count
            total_count_list.append([created_date,total_count])
            print(created_date)

        total_count_list_json=json.dumps(total_count_list)

        total_messages=total_obj.count()
        total_messages_json=json.dumps(total_messages)

        total_true_messages=total_obj.filter(reply_status=True).count()
        total_true_messages_json=json.dumps(total_true_messages)

        total_failed_messages=total_obj.filter(reply_status=False).count()
        total_failed_messages_json=json.dumps(total_failed_messages)

        return render(request,'chat_app/date_graph.html',{'total_count_list_json':total_count_list_json,'from_date':from_date,'to_date':to_date,'total_messages_json':total_messages_json,'total_true_messages_json':total_true_messages_json,'total_failed_messages_json':total_failed_messages_json})

    return render(request,'chat_app/date_graph.html',{'total_count_list_json':total_count_list_json,'from_date':"Select",'to_date':"Select",'total_messages_json':total_messages_json,'total_true_messages_json':total_true_messages_json,'total_failed_messages_json':total_failed_messages_json})
