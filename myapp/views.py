from django.shortcuts import render, HttpResponse

# Create your views here.
def setsession(request):
    request.session['name'] = 'sonam'
    return render(request, 'setsession.html')

def getsession(request):
    if 'name' in request.session:
        n = request.session['name']
        request.session.modified = True
        return render(request, 'getsession.html', {'n':n})
    else:
        return HttpResponse('Your session has been expired')

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')