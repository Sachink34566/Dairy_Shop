from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForms, PasswordReset
urlpatterns = [
    path("",views.home,name='home'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.ProfileView.as_view(), name='address'),
    path("about/",views.About,name='about'),
    path("contact/",views.Contact,name='contact'),
    path("service/",views.Service,name='service'),
    path("register/",views.CustomerRegisterViews.as_view(),name='register'),
    path("category/<slug:val>",views.Category.as_view(),name='category'),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name='product-detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForms), name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'), 
    path("category-title/<val>",views.CategoryTitle.as_view(),name='category-title'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
