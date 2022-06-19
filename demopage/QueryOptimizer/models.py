from django.db import models

# Create your models here.
class Query(models.Model):
    query_sentence=models.CharField(max_length=1000)
    random_page_cost_1=models.BooleanField(default=0)
    random_page_cost_2=models.BooleanField(default=0)
    random_page_cost_4=models.BooleanField(default=0)
    random_page_cost_8=models.BooleanField(default=0)
    random_page_cost_16=models.BooleanField(default=0)
    random_page_cost_32=models.BooleanField(default=0)

    def __str__(self):
        return self.goal