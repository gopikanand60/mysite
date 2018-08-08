from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def TurnOFF1(request):
    return render(request, 'personal/status.html', {'content':['The first node is now turned off in the HES Scholar Room']})

def TurnOFF2(request):
    return render(request, 'personal/status.html', {'content':['The second node is now turned off in the HES Scholar Room']})

def TurnOFF3(request):
    return render(request, 'personal/status.html', {'content':['The third node is now turned off in the HES Scholar Room']})

def TurnOFFS(request):
    return render(request, 'personal/status.html', {'content':['Everything is now turned off in the HES Scholar Room']})
