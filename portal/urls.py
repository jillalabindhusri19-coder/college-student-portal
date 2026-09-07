from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Student
    path('student/', views.student_portal, name='student_portal'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('timetable/', views.timetable, name='timetable'),
    path('room-no/', views.room_no, name='room_no'),
    path('notes/', views.notes, name='notes'),
    path('coordinators/', views.coordinators, name='coordinators'),

    # Previous Year Question Papers - Student
    path(
        'question-papers/',
        views.question_papers,
        name='question_papers'
    ),

    # Faculty
    path('faculty-login/', views.faculty_login, name='faculty_login'),
    path('faculty-dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('upload-timetable/', views.upload_timetable, name='upload_timetable'),
    path('upload-notes/', views.upload_notes, name='upload_notes'),
    path(
        'upload-question-paper/',
        views.upload_question_paper,
        name='upload_question_paper'
    ),
    path('faculty-logout/', views.faculty_logout, name='faculty_logout'),
]