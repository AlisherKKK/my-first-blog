from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect

from .models import Person, Experience, Education, Skills

from django.urls import reverse

def index(request):
	all_humans = Person.objects.all()
	return render(request, 'blogs/list.html', {'list_of_person':all_humans})

def detail(request, blog_id):
	try:
		a=Person.objects.get(id=blog_id)
	except:
		raise Http404("No man!")

	ed=a.education_set.all()
	ex=a.experience_set.all()
	sk=a.skills_set.all()
	
	return render(request, 'blogs/info.html',{'information': a, 'education':ed, 'experience': ex, 'skill':sk})

def add_person(request):
	try:
		a=Person(p_full_name=request.POST['name'],p_information=request.POST['info'], p_date_birth=request.POST['birthday'])
		a.save()
	except:
		raise Http404("No man!")

	return detail(request, Person.objects.count())

def add_educate(request, blog_id):
	try:
		a=Person.objects.get(id=blog_id)
	except:
		raise Http404("No man!")

	a.education_set.create(e_start=request.POST['from'], e_end=request.POST['due'], e_place=request.POST['place'])

	return HttpResponseRedirect(reverse('blogs:detail', args=(a.id,)))

def add_experience(request, blog_id):
	try:
		a=Person.objects.get(id=blog_id)
	except:
		raise Http404("No man!")

	a.experience_set.create(ed_start=request.POST['from'], ed_end=request.POST['due'], ed_place=request.POST['place'])

	return HttpResponseRedirect(reverse('blogs:detail', args=(a.id,)))

def add_skills(request, blog_id):
	try:
		a=Person.objects.get(id=blog_id)
	except:
		raise Http404("No man!")

	a.skills_set.create(s_name=request.POST['name'], s_percent=request.POST['perc'])

	return HttpResponseRedirect(reverse('blogs:detail', args=(a.id,)))
