from django.apps import AppConfig
from transformers import pipeline, BertTokenizer, BertForSequenceClassification

# tokenizer = BertTokenizer.from_pretrained("/Users/jinseo/Demopage/demopage/QueryOptimizer/pretrained_model/vocab.txt")
    
class QueryoptimizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QueryOptimizer'
    predict_model=BertForSequenceClassification.from_pretrained('/Users/jinseo/Demopage/demopage/QueryOptimizer/pretrained_model'
    )

# /Users/jinseo/miniforge3/envs/ftvenv/bin/python manage.py runserver