from django.shortcuts import render
from Citadel.models import NewsMessage, UserProfile, BankingDetails, removeCharactersMessage, removeCharactersName
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import UserForm, UserProfForm, UserLogin, MessageForm, CitizenForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'citadel/index.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

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
                user.is_active=False
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
                    return HttpResponse("Your user has not yet been approved by an administrator.")
            else:
                return HttpResponse("Invalid login details supplied!")
    else:
        user_login = UserLogin()

    return render(request, 'citadel/login.html', {"user_login" : user_login})

@login_required
def user_profile(request):
    current_user = request.user
    if current_user.is_authenticated():
        u = UserProfile.objects.all().get(user=current_user)
        context_dict = {'name': u.name, 'surname': u.surname, 'email': current_user.email,}
        return render(request, 'citadel/profile.html', context_dict)
    else:
        return HttpResponseRedirect('/')

def messageView(request):
    news = NewsMessage.objects.order_by('-time')
    for new in news:
        new.title = removeCharactersMessage(new.title)
        new.message = removeCharactersMessage(new.message)
    return render(request, 'citadel/messagesView.html', {"messages":news, "is_logged_in":request.user.is_authenticated()})

@login_required
def addMessage(request):
    if request.method == 'POST':
        messageForm = MessageForm(data=request.POST)
        if messageForm.is_valid():
            message = messageForm.save(commit=False)
            message.poster = request.user
            message.save()
            return HttpResponseRedirect("/messages/")
    else:
        messageForm = MessageForm()

    # Render the template depending on the context.
    return render(request,
            'citadel/messagesAdd.html',
            {'add_msg' : messageForm, 'is_logged_in':request.user.is_authenticated()},)

@login_required
def editCitizen(request, citid):
    citizen = BankingDetails.objects.get(id=citid)
    if request.method == "POST":
        form = CitizenForm(data=request.POST)
        if form.is_valid():
            citizen.name = form.cleaned_data["name"]
            citizen.surname = form.cleaned_data["surname"]
            citizen.Balance = form.cleaned_data["Balance"]
            citizen.save()
            return HttpResponseRedirect("/citizens/")
    else:
        form = CitizenForm({"name":citizen.name, "surname":citizen.surname, "Balance":citizen.Balance})
    return render(request, "citadel/citizenEdit.html", {"edit_c":form})

@login_required
def makeCitizen(request):
    if request.method == "POST":
        form = CitizenForm(data=request.POST)
        if form.is_valid():
            formData = form.save()
            formData.save()
            return HttpResponseRedirect("/citizens/")
    else:
        form = CitizenForm()
    return render(request, "citadel/newCitizen.html", {"edit_c":form})

@login_required
def deleteCitizens(request,citid):
    if request.method == "POST":
        BankingDetails.objects.get(id=citid).delete()
        return HttpResponseRedirect("/citizens/")
    else:
        citizen = BankingDetails.objects.get(id=citid)
        return render(request, "citadel/citizenDeleteConfirm.html", {"citizen":citizen})

@login_required
def seeCitizens(request):
    citizens = BankingDetails.objects.order_by("-name")
    for citizen in citizens:
        citizen.name = removeCharactersName(citizen.name)
        citizen.surname = removeCharactersName(citizen.surname)
    return render(request, "citadel/people.html", {"citizens":citizens, "is_logged_in":request.user.is_authenticated()})