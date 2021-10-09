from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

path('login/', views.loginUser, name='login'),
path('logout/', views.logoutUser, name='logout'),
path('register/', views.registerUser, name='register'),


path('', views.profiles, name="profiles"),
path('profile/<str:pk>', views.userProfile, name="user_profile"),
path('account/', views.userAccount, name='account'),

path('edit-account/', views.editAccount, name='edit-account'),
path('create-skill/', views.createSkill, name='create_skill'),

path('update-skill/<str:pk>', views.updateSkill, name='update_skill'),
path('delete-skill/<str:pk>', views.deleteSkill, name='delete_skill'),




path('inbox/', views.inbox, name="inbox"),
path('message/<str:pk>', views.viewMessage, name="message"),
path("send-message/<str:pk>/",views.createMessage, name="create_message"),



path('reset_password/',auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name= "reset_password"),
path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password_form.html"), name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_done.html"), name= "password_reset_complete"),


] 