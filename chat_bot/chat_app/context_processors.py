from .models import Statement,Message

def count_message_activites(request):
	message_obj=Message.objects.all()
	total_messages_activites_count=message_obj.count()
	success_messaages_activites_count=message_obj.filter(reply_status=True).count()
	failure_messaages_activites_count=message_obj.filter(reply_status=False).count()
	return {"total_messages_activites_count": total_messages_activites_count,"success_messaages_activites_count":success_messaages_activites_count,"failure_messaages_activites_count":failure_messaages_activites_count}
