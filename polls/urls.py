from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('deepthoughts/', views.DeepthoughtsView.as_view(), name ='Deepthoughts'),
	path('deepthoughts/list', views.DeepthoughtsListView.as_view(), name='DeepthoughtsList'), # changes view to as view bc using CreateVIew
 	path('deepthoughtsubmission', views.submitThought, name='DeepthoughtSubmission')
]
