from django.shortcuts import render

posts = [
	{
		'author': 'AndrewWB',
		'title' : 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'December 25, 2018'
	},
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'December 26, 2018'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})