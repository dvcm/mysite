from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Choice, Poll

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list }
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
    return HttpResponse("Wyniki ankiety %s!" %poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render(request, 'polls/detail.html', {
            'poll':p,
            'error_message':"Nie wybrałeś żadnej opcji.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponse(reverse('polls:results', args=(p.id,)))
