from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def createq(request):
#     return render(request,'polls/createquestion.html',{'all_q':Question.object.all()})

# def addq(request):
#     q = Question(question_text=request.POST['addquestion'],pub_date=timezone.now())
#     q.save()
#     q_add = request.POST['addquestion']+'\'has been add.'
#     return render(request,'polls/createquestion.html',
#         {'all_q':Question.object.all(),'alert_message':q_add})
    

def removequestion(request):
    question = Question.objects.all()
    q_select = Question.objects.get(id=request.POST['question'])
    q_select.delete()

    return HttpResponseRedirect(reverse('polls:index'))

def Add(request):
    q = Question(question_text=request.POST['addq'], pub_date=timezone.now())
    q.save()
    return HttpResponseRedirect(reverse('polls:index'))