from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .predict import test_sentences

# Create your views here.

def enter_query(request):
    query_input=Query()
    if request.method=='POST':
        query_input.query_sentence=request.POST['queryInput']
        query_input.save()
        return redirect('/result/'+str(query_input.id))
    return render(request, 'input.html')

def predict(request, id):
    query_input=get_object_or_404(Query, pk=id)
    result_cost=test_sentences(query_input)
    query_input.save()
    return render(request, 'result.html', {'random_page_cost':result_cost})