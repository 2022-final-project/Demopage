from django.apps import AppConfig
from transformers import pipeline, BertTokenizer, BertForSequenceClassification, AutoTokenizer

class QueryoptimizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QueryOptimizer'
    predict_model=BertForSequenceClassification.from_pretrained('/Users/jinseo/Demopage/demopage/QueryOptimizer/pretrained_model'),
    tokenizer = AutoTokenizer.from_pretrained('/Users/jinseo/Demopage/demopage/QueryOptimizer/pretrained_tokenizer')

# /Users/jinseo/miniforge3/envs/ftvenv/bin/python manage.py runserver