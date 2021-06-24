from django.urls import path
from app import views


urlpatterns = [
    path('', views.RedirectView.as_view(pattern_name='students'), name='app'),
    path('students/<int:pk>/', views.student.as_view(template_name = 'app/students.html'),name='students'),
    path('students/', views.show_students.as_view(template_name='app/showstudents.html'), name='students'),
    path('message/', views.message_page.as_view(), name='message'),
    path('form/', views.student_form.as_view(), name='form'),
    path('update/<int:pk>/', views.student_update.as_view(), name='update'),
    path('delet/<int:pk>/', views.delet_page.as_view(), name='delet'),
    path('thanks/', views.thanks_page.as_view(), name='thanks')

]

