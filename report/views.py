from django.shortcuts import render


def home(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
    return render(request, "report/home.html", context)