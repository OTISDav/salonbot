from django.contrib import admin
from django.urls import path, include
from bot.api.webhooks import whatsapp_webhook

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("webhook/whatsapp/", whatsapp_webhook),
    path("dashboard/", include("bot.adminpanel.urls")),

    # Login / Logout pour tests
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/accounts/login/"), name="logout"),
]
