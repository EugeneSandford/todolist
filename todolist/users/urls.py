from django.urls import path
from .views import MyLoginView, logout_view, RegisterView, ProfileView
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [

    # Gestion du Profil
    path('profile/', ProfileView.as_view(), name='profile'),

    # Gestion des login, logout, register et reset de password
    path('login/', 
        MyLoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True),
        name='login'),
    
    # Normalement, la classe LogoutView aurait du être utilisée.
    # Cependant, il y a eu un souci de sécurité critique avec, et
    # du coup, il faut réutiliser les fonctions plutot que les classes.
    #   Voir la fonction logout dans 'views.py' qui fait un logout simple et 
    #   une redirection vers 'home'.
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='users/password_reset.html',
            html_email_template_name='users/password_reset_email.html'
        ),
        name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]

