from django.http import HttpResponse

# Create your views here.¨
def index(request):
    return HttpResponse("Здраствуй Мыр. You are at the polls index.")

def results(request, question_id):
    response = 'Hledíš na rizalts of kvesčn %s'
    return HttpResponse(response % question_id)

def detail(request, question_id):
    return HttpResponse('Koukáš na otázku %s.' % question_id)

def vote(request, question_id):
    return HttpResponse('júá voting on question %s' % question_id)