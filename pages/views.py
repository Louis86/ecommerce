from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #
    #return HttpResponse("<h1> Homepage</h1>")
    #pagename = '/'+pagename
    #pg = Page.objects.get(permalink=pagename)
    #context =  {
    #    'title': pg.title,
    #    'content': pg.bodytext,
    #    'last_updated': pg.update_date,

    #}
    #return render(request, 'pages/page.html',context)
    return render(request, 'pages/page.html')
