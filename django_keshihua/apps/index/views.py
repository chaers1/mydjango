from django.shortcuts import render, redirect


def index(request):
    username = request.session.get('username')
    return render(request, 'index_sucess.html', {'username': username})


def logout(request):
    return redirect('login')
