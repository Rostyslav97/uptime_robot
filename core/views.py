from core.services import Checker
from django.http import HttpResponse

def foo(request):
    checker = Checker()
    checker.generate_reports()
    return HttpResponse("Done")