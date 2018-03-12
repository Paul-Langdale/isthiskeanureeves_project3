from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return index(request)
def index(request):
    context_dict = {	'boldmessage' : "This is a django variable test",
	'keanuimg1': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Keanu_Reeves_2014.jpg/220px-Keanu_Reeves_2014.jpg" 
	}
    return render(request, 'isthiskeanureeves/index.html',context_dict)
	
def keanew(request):
    return HttpResponse("This is the kea-new page")
def about(request):
    return HttpResponse("This is the about page")
def topkeanu(request):
    return HttpResponse("This is the top-keanu page")
def keanothim(request):
    return HttpResponse("This is the kea-not-him page")
def login(request):
    return HttpResponse("This is the login page")
def upload(request):
    return HttpResponse("This is the upload page")

#this needs	to fully converted to work with the post <title> pages
#@login_required
def post(request,post_title_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
#wip^