# # [platform: ACTIONS_ON_GOOGLE
# # simple_responses {
# #   simple_responses {
# #     text_to_speech: "krishna gopal dubey"
# #   }
# # }
# # , 
# # platform: ACTIONS_ON_GOOGLE
# # suggestions {
# #   suggestions {
# #     title: "krishna"
# #   }
# #   suggestions {
# #     title: "gopal"
# #   }
# #   suggestions {
# #     title: "dubey"
# #   }
# #   suggestions {
# #     title: "raj"
# #   }
# # }
# # , text {
# #   text: "krishna gopal dubey"
# # }
# # ]

# # platform: ACTIONS_ON_GOOGLE
# # simple_responses {
# #   simple_responses {
# #     text_to_speech: "krishna gopal dubey"
# #   }
# # }



# # def json_dict(fullfillment_text, rich_list):
# #     x1={}
# #     x1["platform"]="ACTIONS_ON_GOOGLE"
# #     x_d1={}
# #     x_d1["textToSpeech"]=fullfillment_text
# #     xl=[x_d1]
# #     x_d2={}
# #     x_d2['simpleResponses']=xl
# #     x1["simpleResponses"]=x_d2

# #     y1={}
# #     y1["platform"]="ACTIONS_ON_GOOGLE"
# #     yl1=[]
# #     for riches in rich_list:
# #         y_d2={}
# #         y_d2['title']=riches
# #         yl1.append(y_d2)
# #     y_d1={}
# #     y_d1['suggestions']=yl1
# #     y1["suggestions"]=y_d1

# #     d={}
# #     d['fulfillmentText']=fullfillment_text
# #     l1=[x1,y1]
# #     d['fulfillmentMessages']=l1
# #     return d


# # function callbuttonfunction() {
# #             var buttons = document.querySelectorAll('button');
# #             console.log(buttons)
# #             for (var i=0; i<buttons.length; ++i) {
# #                   buttons[i].addEventListener('click', clickFunc);
# #                 }
            
# #             function clickFunc() {
# #                 var button_value = document.getElementById(this.id).innerHTML;
# #                 getBotResponse(button_value) 
# #                 }    
# #             // console.log("<==========buttons===========>")
# #             // console.log(buttons)
# #             // console.log("<===================================>")
# #             // console.log("<==========button_value===========>")
# #             // console.log(button_value)
# #             // console.log("<===================================>")
# #             // var button_value = document.getElementById("Django").innerHTML;
# #             // getBotResponse(button_value)
# #           }

# # def home(request):
# #     return render(request, "chat_app/home_copy.html")
# # path('home/',  views.home, name='home'),

# # def request_data(request):
# #     context={}
# #     return render(request, "chat_app/chat.html",context)
# # path('request_data/',  views.request_data, name='request_data'),

# @csrf_exempt
# @require_http_methods(['POST'])
# def index_example(request):
#     print("=======================>")
#     print(request)
#     print(request.body)
#     input_dict = convert(request.body)
#     print("input_dict==========>",input_dict)
#     input_text = json.loads(input_dict)['name']
#     print("input_text=========>",input_text)
#     print("=======================>")
#     return HttpResponse("Hello, world. You're at the polls index.")
# path('index_example/',  views.index_example, name='index_example'),

# @csrf_exempt
# def webhook(request):
#     req = json.loads(request.body)
#     action = req.get('queryResult').get('action')
#     print("action=====>",action)
#     fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
#     print("fulfillmentText====>",fulfillmentText)
#     return JsonResponse(fulfillmentText, safe=False)
####################################

# {
#     "responseId": "*****************************",
#     "queryResult": {
#         "queryText": "actions_intent_TRANSACTION_REQUIREMENTS_CHECK",
#         "parameters": {},
#         "allRequiredParamsPresent": true,
#         "fulfillmentText": "HERE",
#         "fulfillmentMessages": [
#             {
#                 "text": {
#                     "text": [
#                         "HERE"
#                     ]
#                 }
#             }
#         ],
#         "outputContexts": [
#             {
#                 "name": "*****************************"
#             },
#             {
#                 "name": "*****************************"
#             },
#             {
#                 "name": "*****************************"
#             },
#             {
#                 "name": "*****************************"
#             },
#             {
#                 "name": "*****************************"
#             },
#             {
#                 "name": "*****************************",
#                 "parameters": {
#                     "TRANSACTION_REQUIREMENTS_CHECK_RESULT": {
#                         "@type": "type.googleapis.com/google.actions.v2.TransactionRequirementsCheckResult",
#                         "resultType": "OK"
#                     }
#                 }
#             }
#         ],
#         "intent": {
#             "name": "*****************************",
#             "displayName": "Int2"
#         },
#         "intentDetectionConfidence": 1,
#         "diagnosticInfo": {},
#         "languageCode": "en-us"
#     },
#     "originalDetectIntentRequest": {
#         "source": "google",
#         "version": "2",
#         "payload": {
#             "isInSandbox": true,
#             "surface": {
#                 "capabilities": [
#                     {
#                         "name": "actions.capability.WEB_BROWSER"
#                     },
#                     {
#                         "name": "actions.capability.MEDIA_RESPONSE_AUDIO"
#                     },
#                     {
#                         "name": "actions.capability.SCREEN_OUTPUT"
#                     },
#                     {
#                         "name": "actions.capability.AUDIO_OUTPUT"
#                     }
#                 ]
#             },
#             "inputs": [
#                 {
#                     "rawInputs": [
#                         {
#                             "inputType": "KEYBOARD"
#                         }
#                     ],
#                     "arguments": [
#                         {
#                             "extension": {
#                                 "@type": "type.googleapis.com/google.actions.v2.TransactionRequirementsCheckResult",
#                                 "resultType": "OK"
#                             },
#                             "name": "TRANSACTION_REQUIREMENTS_CHECK_RESULT"
#                         }
#                     ],
#                     "intent": "actions.intent.TRANSACTION_REQUIREMENTS_CHECK"
#                 }
#             ],
#             "user": {
#                 "lastSeen": "2018-05-16T11:15:14Z",
#                 "locale": "en-US",
#                 "userId": "*****************************"
#             },
#             "conversation": {
#                 "conversationId": "1526470000479",
#                 "type": "ACTIVE",
#                 "conversationToken": "[]"
#             },
#             "availableSurfaces": [
#                 {
#                     "capabilities": [
#                         {
#                             "name": "actions.capability.SCREEN_OUTPUT"
#                         },
#                         {
#                             "name": "actions.capability.AUDIO_OUTPUT"
#                         }
#                     ]
#                 }
#             ]
#         }
#     },
#     "session": "*****************************"
# }

 # krishna.g@hushmail.com
 # krishna.g@hushmail.com


  # htmly  = get_template()
  #   my_url = "https://0386a573dda3.ngrok.io/chat_app/show_all_messages/"
  #   d = {'my_url':my_url,"body":"krishna gopal dubey"}
  #   html_content = htmly.render(d)
  #   print(html_content)
  #   msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
  #   msg.attach_alternative(html_content, "text/html")
  #   msg.content_subtype = "html"  # Main content is now text/html
  #   msg.send()

    # text_content = 'required details about the link'
    # html_content='''<a href="https://0386a573dda3.ngrok.io/chat_app/show_all_messages/">Click</a>'''
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.content_subtype = "html"
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()

    # msg = EmailMessage(subject, html_content, from_email, [to])
    # msg.send()

    # html_content= render_to_string(
    #     '''''',
    #         )
    # send_mail('subject', 
    #         "KRISHNA GOPAL DUBEY",
    #         html_content,
    #         'krishna.g@hushmail.com', 
    #         ['krgopald92@gmail.com',])


# def second_mail_data(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         message = render_to_string("chat_app/check_email.html")
#         plain_message = strip_tags(message)
#         print("plain_message=====>",plain_message)
#         send_mail('Contact Form',
#          plain_message, 
#          'krishna.g@hushmail.com',
#          ['krgopald92@gmail.com',], 
#          fail_silently=True)
#     return render(request, 'chat_app/index.html')
#     
###################
# from django.core.mail import send_mail
# from django.core import mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.template.loader import render_to_string, get_template
# from django.core.mail import EmailMultiAlternatives,EmailMessage



# def send_main_method(request):
#     subject = 'Subject'
#     html_message = render_to_string("chat_app/check_email.html")
#     print("html_message===>",html_message)
#     subject, from_email, to = 'hello', 'krishna.g@hushmail.com','krgopald92@gmail.com'
#     plain_message = strip_tags(html_message)
#     print("plain_message====>",plain_message)
    
#     mail.send_mail(subject, html_message, from_email, [to], html_message=html_message)
    # return render(request, "chat_app/show_all_messages.html")



# path('send_main_method/',  views.send_main_method, name='send_main_method'),
#     path('second_mail_data/',  views.second_mail_data, name='second_mail_data'),    



# <h3>Contact Form</h3>

# <form method="post" action="{% url 'second_mail_data' %}">
# 	{% csrf_token %}
# 	<textarea name="message" placeholder="Message..."></textarea>
# 	<input type="submit" />
# </form>