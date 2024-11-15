from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import CustomUser


# This function provides the implementation for creating a user in azure sql database. 
@receiver(post_save, sender=CustomUser)
def createUserAzure(sender, instance, created, **kwargs):
    if created:
        cursor = connection.cursor()

        try:
            cursor.execute("""INSERT INTO dbo.users (username, _name, email, _password, tutor_status) VALUES(%s, %s, %s, %s)
            """, [instance.username, instance.name, instance.password, instance.password], '0')
            connection.commit()
        except Exception as e:
            print(f"Error inserting into azure: {e}")
            connection.rollback()
        finally:
            connection.close()