from  django.http import  HttpResponse

def index(request):
    return HttpResponse("<h1> Welcome!!! You can.Let\'s start.</h1><h1> Welcome!!! You can.Let\'s start.</h1><h1>"
                        " Welcome!!! You can.Let\'s start.</h1><h1>"
                        " Welcome!!! You can.Let\'s start.</h1>")