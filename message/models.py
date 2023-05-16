from django.db import models

# Create your models here.


class Message(models.Model):
    print('started message model')
    id = models.BigAutoField(primary_key=True)

    messages = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'message_message'
    print('ended message model')

# class MessageMessage(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     message = models.CharField(max_length=300)

#     class Meta:
#         managed = False
#         db_table = 'message_message'
