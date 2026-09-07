from django.contrib import admin

from .models import Faculty, Subject, Timetable, Notes


# =========================
# FACULTY ADMIN
# =========================
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'user',
    )


# =========================
# SUBJECT ADMIN
# =========================
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        'subject_name',
        'branch',
        'year',
        'semester',
        'coordinator',
    )


# =========================
# TIMETABLE ADMIN
# =========================
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        'branch',
        'year',
        'section',
        'semester',
        'room_no',
        'faculty',
        'uploaded_at',
    )


# =========================
# NOTES ADMIN
# =========================
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):

    list_display = (
        'subject_name',
        'branch',
        'year',
        'section',
        'semester',
        'faculty',
        'uploaded_at',
    )