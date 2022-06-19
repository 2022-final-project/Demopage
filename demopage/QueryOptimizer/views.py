from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .running_model import test_sentences
from .preprocessing import table_column_preprocessing

# Create your views here.

def enter_query(request):
    query_input=Query()
    if request.method=='POST':
        query_input.original_query_input=request.POST['queryInput']
        query_input.save()
        return redirect('/result/'+str(query_input.id))
    return render(request, 'input.html')

def predict(request, id):
    query_input=get_object_or_404(Query, pk=id)
    query_input.query_sentence=table_column_preprocessing(query_input.original_query_input) # table, column 전처리
    result_cost=test_sentences(query_input.query_sentence) # return type : [0, 0, 0, 0, 0, 0]

    if result_cost[0]==1: query_input.random_page_cost_1=1
    if result_cost[1]==1: query_input.random_page_cost_2=1
    if result_cost[2]==1: query_input.random_page_cost_4=1
    if result_cost[3]==1: query_input.random_page_cost_8=1
    if result_cost[4]==1: query_input.random_page_cost_16=1
    if result_cost[5]==1: query_input.random_page_cost_32=1
    query_input.save()

    print(query_input.query_sentence)

    return render(request, 'result.html', result={'result':query_input})