from django.urls import path

from wings import views

urlpatterns = [
    path('<name>/', views.RaidListView.as_view()),
    ]