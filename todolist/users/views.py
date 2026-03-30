
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.


# Normalement, la classe Logoutview aurait du être utilisée pour se déconnecter.
# Cependant, il y a eu un souci de sécurité critique avec, et
# du coup, il faut réutiliser les fonctions plutot que les classes.
#   D'où la fonction logout dans 'views.py' qui fait un logout simple et 
#   une redirection vers 'home'.
def logout_view(request):
    logout(request)
    return render(request, 'home.html', {})

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)