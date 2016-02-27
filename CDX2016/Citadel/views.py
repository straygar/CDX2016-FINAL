from django.shortcuts import render
from Citadel.models import NewsMessage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import UserForm, UserProfile, UserProfForm, User
from django.http import HttpResponse

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
                user = user_form.save()
                user.set_password(user.password)
                user_prof_form.save()
                user.save()
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
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'citadel/login.html', {})


def user_profile(request):
    current_user = request.user
    u = UserProfile.objects.filter(user == current_user)
    print u
#    context_dict = {'profile_details' = u}
    return render(request, 'citadel/profile.html', context_dict)



@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
