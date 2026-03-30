from django.urls import path
from .views import MyLoginView, logout_view, RegisterView

urlpatterns = [
    path('login/', 
        MyLoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True),
        name='login'),
    # Normalement, la classe Logoutview aurait du être utilisée.
    # Cependant, il y a eu un souci de sécurité critique avec, et
    # du coup, il faut réutiliser les fonctions plutot que les classes.
    #   Voir la fonction logout dans 'views.py' qui fait un logout simple et 
    #   une redirection vers 'home'.
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterView.as_view(),name='register'),

]
 