from chat_app.models import Statement,Message,Owner_Handling_Message

def get_length_for_formset():
    list_of_question=[]
    owner_handling_message_obj=Owner_Handling_Message.objects.filter(owner_response="no response")
    for question in owner_handling_message_obj:
        list_of_question.append(question.statement.text)
    return list_of_question   