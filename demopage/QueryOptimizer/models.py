from django.db import models

# Create your models here.
class Query(models.Model):
    original_query_input=models.CharField(max_length=1000, default='') # before preprocessing
    query_sentence=models.CharField(max_length=1000) # after preprocessing
    random_page_cost_1=models.BooleanField(default=0)
    random_page_cost_2=models.BooleanField(default=0)
    random_page_cost_4=models.BooleanField(default=0)
    random_page_cost_8=models.BooleanField(default=0)
    random_page_cost_16=models.BooleanField(default=0)
    random_page_cost_32=models.BooleanField(default=0)
