from django.db import models

# Create your models here.
class Query(models.Model):
    query_sentence=models.CharField(max_length=1000)
    random_page_cost=models.FloatField(default=4.0)

    def __str__(self):
        return self.goal