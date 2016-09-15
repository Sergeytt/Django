from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comment

# Create your views here.

def basic_one(request):
	view = 'basic_one'
	html = '<html><body>This is %s view</body></html>' % view
	return HttpResponse(html)

def template_two(request):
	view = 'template_two'
	temp = get_template('mypage.html')
	html = temp.render(Context({'name': view}))
	return HttpResponse(html)

def template_three(request):
	view = 'template_three'
	return render_to_response('mypage.html', {'name': view})

def articles(request):
	return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id=1):
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comment.objects.filter(comments_article_id=article_id)})



