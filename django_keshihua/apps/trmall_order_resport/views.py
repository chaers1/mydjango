from django.shortcuts import render

# Create your views here.


def tianmao(request):
    clums = dict()
    username = request.session.get('username')
    clums['username'] = username

    return render(request,'tianmao_html.html',clums)