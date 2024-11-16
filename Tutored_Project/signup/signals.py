from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_azure_user(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a user in the Azure SQL database
    whenever a new CustomUser is created.
    """
    if created:
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO dbo.users (username, _name ,email, _password, tutor_status)
                VALUES (%s, %s, %s, %s, 0)
            """, [instance.username, instance.name, instance.email, instance.password,])
            connection.commit() 
        except Exception as e:
            print(f"Error creating user in Azure SQL: {e}")
            connection.rollback()  
