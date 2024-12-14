
from django.contrib import admin
from django.urls import path
import main.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path("dashboard/", views.dashboard),
    path("pre/", views.predashboard),
    path("createuser/", views.create_user),
    path("createpayment/<int:amount>/", views.create_payment),
    path('flashcards/', views.flashcards),
    path('view-key/', views.display_key)
    # path('signup/', views)
]
