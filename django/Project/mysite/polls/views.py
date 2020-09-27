from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Questions


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def votes(request,question_id):

