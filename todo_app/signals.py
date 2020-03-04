from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from todo_app.models import Key
from todo_app.tasks import addkey, deletekey
from threading import Thread

print("SIGNALLLL")


@receiver(post_save, sender=Key,dispatch_uid="start_task")
def start_task(sender, instance, created, **kwargs):
    if created:
        background_job = Thread(target=addkey, args=(instance.username.email, instance.type))
        print('ADDED KEY')
        background_job.start()
    else:
        background_job = Thread(target=deletekey, args=(instance.username.email, instance.type))
        print('UPDATED KEY')
        background_job.start()

@receiver(pre_delete, sender=Key)
def Delete(sender, instance, using, **kwargs):
    if using:
        background_job = Thread(target=deletekey, args=(instance.username.email, instance.type))
        background_job.start()
        print("DELETED KEY")

