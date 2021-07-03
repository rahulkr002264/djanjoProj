from django.urls import path
from bankapp import views

urlpatterns = [
    path('homepage/',views.homepage),
    path('new_user_form/', views.new_user),
    path("user_form_submit/",views.create_user),
    path('register/',views.register),
    path('new_registration_detail/',views.new_registration),
    path('login_form/',views.login_form),
    path('login/',views.login),
    path('logout1/',views.logout1),

    path('show_details/',views.show_details),
]
