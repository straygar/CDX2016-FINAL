from django.shortcuts import render
from Citadel.models import NewsMessage, UserProfile, BankingDetails
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import UserForm, UserProfForm, UserLogin
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    news = NewsMessage.objects.order_by('-time')[:5]
    context_dict = {'news': news}
    return render(request, 'citadel/index.html', context_dict)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Citadel/')

def registerFirst(request):
    return render(request, 'citadel/registerFirst.html', {})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_prof_form = UserProfForm(data=request.POST)
        if user_form.is_valid():
            if (user_prof_form.is_valid()):
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.save()
                user_profile = user_prof_form.save(commit=False)
                user_profile.user = user
                user_profile.save()
                registered = True
            else:
                print user_prof_form.errors
        else:
            print user_form.errors
    else:
        user_form = UserForm()
        user_prof_form = UserProfForm()

    # Render the template depending on the context.
    return render(request,
            'citadel/register.html',
            {'user_form': user_form, 'user_prof_form': user_prof_form, 'registered': registered} )

def usrlogin(request):
    if request.method == 'POST':
        user_login = UserLogin(data=request.POST)
        if (user_login.is_valid()):
            user = authenticate(username=user_login.cleaned_data["username"], password=user_login.cleaned_data["password"])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("")
            else:
                return HttpResponse("Invalid login details supplied.")
        #else:
            #print user_login.errors
    else:
        return render(request, 'citadel/login.html', {"user_login" : UserLogin()})
    return HttpResponseRedirect("/Citadel/")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

#@login_required
def user_profile(request):
    current_user = request.user
    print current_user
    if current_user.is_authenticated:
        u = UserProfile.objects.all().get(user=current_user)
        print u
        context_dict = {'name': u.name,
                    'surname': u.surname
                        }
        return render(request, 'citadel/profile.html', context_dict)
    else:
        return HttpResponseRedirect('/')
