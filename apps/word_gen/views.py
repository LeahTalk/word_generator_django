from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime

from django.utils.crypto import get_random_string

def index(request):
    if "attempts" not in request.session or "randomWord" not in request.session:
        request.session['attempts'] = 1
        request.session['randomWord'] = get_random_string(length=14)
    else:
        request.session['attempts'] += 1
        request.session['randomWord'] = get_random_string(length=14)
    print(request.session['attempts'])
    print(request.session['randomWord'])
    return render(request, 'word_gen/index.html')

def reset(request):
    request.session['attempts'] = 0
    return redirect('/random_word')