from django.db import models

# Create your models here.



class cafe_info(models.Model):
    class Meta:
        db_table = 'cafe_info'
        app_label = 'cafelog'
        
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    chain_id = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title