from django.apps import AppConfig
from transformers import pipeline, BertForSequenceClassification

class QueryoptimizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QueryOptimizer'
    predict_model=pipeline("question-answering", 
    model=BertForSequenceClassification.from_pretrained('/Users/jinseo/Demopage/demopage/QueryOptimizer/predict_model'),
    tokenizer="/Users/jinseo/Demopage/demopage/QueryOptimizer/predict_model"
    )

# /Users/jinseo/miniforge3/envs/ftvenv/bin/python manage.py runserver