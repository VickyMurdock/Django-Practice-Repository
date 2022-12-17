from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.views.generic.edit import CreateView
# from django.views.generic.list import ListView

from .models import Choice, Question, Deepthoughts


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



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
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class DeepthoughtsView(generic.ListView): # changed this from DetailView to View, bc I didn't want a pk value
	model = Deepthoughts
	template_name = 'polls/deepthoughts/deepthoughts_form.html'
#	fields = ['deepthoughts_title', 'deepthoughts_text']



class DeepthoughtsListView(generic.ListView):
	# model = Deepthoughts
	template_name = 'polls/deepthoughts/deepthought_list.html'
	context_object_name = 'DeepthoughtsList'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Deepthoughts.objects.all()


	#deepthought_from deepthought_list





'''
def DeepthoughtsView(request):
	deepthoughts = Deepthoughts()
	deepthoughts.title = request.POST("title")
	deepthoughts.text = request.POST("dthought")
	deepthoughts.save()
	return render(request, 'polls/deepthoughts/deepthoughts_form.html')

'''

def submitThought(request):
	deepthoughts = Deepthoughts()
	deepthoughts.deepthoughts_title = request.POST["title"]
	deepthoughts.deepthoughts_text = request.POST["dthought"]
	deepthoughts.save()

	return HttpResponseRedirect(reverse('polls:DeepthoughtsList'))






