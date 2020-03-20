from django.urls import path,reverse_lazy
from . import views

from django.contrib.auth import views as auth_views



app_name='accounts'

urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

    path('',views.home,name='home'),
    path('user/',views.userPage,name='user_ page'),

    path('account/',views.accountSettings,name="account"),

    path('customer/<str:pk_test>',views.customer,name='customer'),
    path('products/',views.products,name='products'),


    path('create_order/<str:pk>',views.createOrder,name='create_order'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),
    
    #auth_views
    #submit email form
    
    path('reset_password/',auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),name="reset_password"),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_done'),

    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html", success_url=reverse_lazy('accounts:password_reset_complete')),name='password_reset_done'),


    #submit sent success message
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),    
    #Link to password Rest form in email
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    #password successfully changed message
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
