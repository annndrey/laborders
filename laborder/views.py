# -*- coding: utf-8 -*-


from numpy import array
from django.shortcuts import render_to_response
from laborder.orders.forms import ContactForm, WishForm
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from laborder.orders.models import Stuff, Wish
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def main(request, template_name='login.html'):
    c = {}
    c.update(csrf(request))
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/wishes")
        else:
            c.update({'login_error':u'Попробуйте еще раз'})
            return render_to_response(template_name, c)
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect("/wishes")
        else:
            return render_to_response(template_name, c)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required()
def wishes(request, status):
    print status
    wish_user = Wish.objects.filter(user=request.user.id)
    wish_other = Wish.objects.exclude(user=request.user.id)
    st_dict = {'delete':u'удалена', 'edit':u'изменена', 'add':u'добавлена'}
    if status is not False:
        st = st_dict.get(status, False)
    else:
        st = False

    return render_to_response("wishes.html", {'wishes':wish_user, 'other_wishes':wish_other, 'page_name':u'Список заказов', 'user':request.user, 'status':False})


@login_required()
def delete(request, num):
    #delete object
    #return httpredirect /wishes 
    w = Wish.objects.get(id=num)
    w.delete()
    return HttpResponseRedirect('/wishes')

@login_required()
def edit(request, num):
    wish = Wish.objects.get(id=num)
    form = WishForm(instance=wish)
    if request.method == 'POST':
        f = WishForm(request.POST, instance=wish)
        f.save()
        return HttpResponseRedirect('/wishes')
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response("hello.html", c)

@login_required()
def new(request):
    #lst = request.META.items()
    #if request.method == 'POST':
    #    form = ContactForm(request.POST)
    #    if form.is_valid():
    #        cd = form.cleaned_data
    #        send_mail(
    #            cd['subject'],
    #            cd['message'],
    #            cd.get('email', 'piggy@piggy.thruhere.net'),
    #            ['piggy@piggy.thruhere.net',],
    #            )
    #        return HttpResponseRedirect('/hello')
    #else:
    
    #тут добавить текущего пользователя. Хотя можно
    #его вообще убрать. 
    form = WishForm()
    
    if request.method == 'POST':
        #print request.POST
        f = WishForm(request.POST, instance=Wish())
        new_wish = f.save()
        return HttpResponseRedirect('/wishes')
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response("hello.html", c)

