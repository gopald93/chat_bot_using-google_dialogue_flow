from django.db import models

class Statement(models.Model):
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
       return self.text

class Message(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)
    intent = models.CharField(max_length=100, blank=True)
    reply_status= models.BooleanField(default=False,null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    owner_response=models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.response

class Owner_Handling_Message(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE)
    owner_response=models.TextField(null=True, blank=True,default="no response")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return self.statement.text