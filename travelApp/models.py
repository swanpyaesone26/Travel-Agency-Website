from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=False)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_form_entries'  
        
    def __str__(self):
        return self.name
    
class UserRegisterInfo(models.Model):
    username = models.CharField(max_length=150, unique=True)
    nrc_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        db_table = 'user_register_info'  # Custom table name

    def __str__(self):
        return self.username



