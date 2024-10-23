from django.http import HttpResponse

# Create your views here.¨
def index(request):
    return HttpResponse("Здраствуй Мыр. You are at the polls index.")
