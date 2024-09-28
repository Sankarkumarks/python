Topic: Django Signals

Question 1: 
Django signals are basically excute tasks in synchronous fashion by default. 
Django signals which are enables us to notify specific receivers when certain events happen to senders.
Example:
class MyModel(models.Model):
    name = models.CharField(max_length=100)
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("MyModel is successfully created")
MyModel.objects.create(a = 'hi', b = 'kumar')


Question 2:
Django signals run in the same thread as the caller.
Example:
class MyModel(models.Model):
    name = models.CharField(max_length=100)
@receiver(post_save, sender=MyModel)
def user_saved(sender, instance, **kwargs):
    print(f"Receiver's thread: {threading.current_thread().name}")
print("Sender's thread: {threading.current_thread().name}")
user = User.objects.create(username='testuser')


Question 3:
django signals doesn't run in the same database transaction as the caller by default.
Example:
class MyModel(models.Model):
    name = models.CharField(max_length=100)
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    MyModel.objects.create(name="Another instance")
with transaction.atomic():
    obj = MyModel.objects.create(name="First instance")
