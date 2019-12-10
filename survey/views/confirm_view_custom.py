from django.http import HttpResponseRedirect

def confirm_view_custom(request, *args, **kwargs):
    return HttpResponseRedirect('http://127.0.0.1:8000/survey/1/') 