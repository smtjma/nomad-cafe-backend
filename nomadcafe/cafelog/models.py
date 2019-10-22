from django.db import models

# Create your models here.
import uuid



class Cafeinfo(models.Model):
    class Meta:
        db_table = 'Cafeinfo'
        app_label = 'cafelog'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField
    chain = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title