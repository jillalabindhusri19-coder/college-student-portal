from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Timetable, Subject, Notes, QuestionPaper


# =========================
# HOME PAGE
# =========================

def home(request):
    return render(request, 'portal/home.html')


# =========================
# STUDENT PORTAL
# =========================

def student_portal(request):
    return render(request, 'portal/student_portal.html')


# =========================
# STUDENT DASHBOARD
# =========================

def student_dashboard(request):

    if request.method == 'POST':

        request.session['name'] = request.POST.get('name')
        request.session['branch'] = request.POST.get('branch')
        request.session['section'] = request.POST.get('section')
        request.session['year'] = request.POST.get('year')
        request.session['semester'] = request.POST.get('semester')

    return render(
        request,
        'portal/student_dashboard.html',
        {
            'name': request.session.get('name'),
            'branch': request.session.get('branch'),
            'section': request.session.get('section'),
            'year': request.session.get('year'),
            'semester': request.session.get('semester'),
        }
    )


# =========================
# STUDENT TIMETABLE
# =========================

def timetable(request):

    branch = request.session.get('branch')
    year = request.session.get('year')
    section = request.session.get('section')
    semester = request.session.get('semester')

    timetable_data = Timetable.objects.filter(
        branch=branch,
        year=year,
        section=section,
        semester=semester
    ).order_by('-uploaded_at').first()

    return render(
        request,
        'portal/timetable.html',
        {
            'timetable': timetable_data
        }
    )


# =========================
# ROOM NUMBER
# =========================

def room_no(request):

    branch = request.session.get('branch')
    year = request.session.get('year')
    section = request.session.get('section')
    semester = request.session.get('semester')

    timetable_data = Timetable.objects.filter(
        branch=branch,
        year=year,
        section=section,
        semester=semester
    ).order_by('-uploaded_at').first()

    return render(
        request,
        'portal/room_no.html',
        {
            'timetable': timetable_data
        }
    )


# =========================
# STUDENT NOTES
# =========================

def notes(request):

    branch = request.session.get('branch')
    year = request.session.get('year')
    section = request.session.get('section')
    semester = request.session.get('semester')

    notes_data = Notes.objects.filter(
        branch=branch,
        year=year,
        section=section,
        semester=semester
    ).order_by('-uploaded_at')

    return render(
        request,
        'portal/notes.html',
        {
            'notes_data': notes_data
        }
    )


# =========================
# SUBJECT COORDINATORS
# =========================

def coordinators(request):

    branch = request.session.get('branch')
    year = request.session.get('year')
    semester = request.session.get('semester')

    subjects = Subject.objects.filter(
        branch=branch,
        year=year,
        semester=semester
    ).select_related('coordinator')

    return render(
        request,
        'portal/coordinators.html',
        {
            'subjects': subjects
        }
    )


# =========================
# STUDENT DETAILS
# =========================




# =========================
# FACULTY LOGIN
# =========================

def faculty_login(request):

    # Ask for login again whenever Faculty Portal is opened
    if request.method == 'GET':
        logout(request)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('faculty_dashboard')

        return render(
            request,
            'portal/faculty_login.html',
            {
                'error': '❌ Invalid username or password'
            }
        )

    return render(
        request,
        'portal/faculty_login.html'
    )


# =========================
# FACULTY DASHBOARD
# =========================

def faculty_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('faculty_login')

    return render(
        request,
        'portal/faculty_dashboard.html'
    )


# =========================
# FACULTY LOGOUT
# =========================

def faculty_logout(request):

    logout(request)

    return redirect('faculty_login')


# =========================
# UPLOAD TIMETABLE
# =========================

def upload_timetable(request):

    if not request.user.is_authenticated:
        return redirect('faculty_login')

    if request.method == 'POST':

        branch = request.POST.get('branch')
        year = request.POST.get('year')
        section = request.POST.get('section')
        semester = request.POST.get('semester')
        room_no = request.POST.get('room_no')

        timetable_file = request.FILES.get(
            'timetable_file'
        )

        Timetable.objects.create(
            faculty=request.user.faculty,
            branch=branch,
            year=year,
            section=section,
            semester=semester,
            room_no=room_no,
            timetable_file=timetable_file
        )

        return render(
            request,
            'portal/upload_timetable.html',
            {
                'message':
                    '✅ Time Table uploaded successfully!'
            }
        )

    return render(
        request,
        'portal/upload_timetable.html'
    )


# =========================
# UPLOAD NOTES
# =========================

def upload_notes(request):

    if not request.user.is_authenticated:
        return redirect('faculty_login')

    if request.method == 'POST':

        branch = request.POST.get('branch')
        year = request.POST.get('year')
        section = request.POST.get('section')
        semester = request.POST.get('semester')
        subject_name = request.POST.get('subject')
        notes_pdf = request.FILES.get('notes_pdf')

        faculty = request.user.faculty

        if not subject_name or not notes_pdf:
            return render(
                request,
                'portal/upload_notes.html',
                {
                    'message':
                        '❌ Please enter subject name and select a PDF.'
                }
            )

        Notes.objects.create(
            faculty=faculty,
            branch=branch,
            year=year,
            section=section,
            semester=semester,
            subject_name=subject_name,
            notes_pdf=notes_pdf
        )

        return render(
            request,
            'portal/upload_notes.html',
            {
                'message':
                    '✅ Notes uploaded successfully!'
            }
        )

    return render(
        request,
        'portal/upload_notes.html'
    )
def upload_question_paper(request):
    if not request.user.is_authenticated:
        return redirect('faculty_login')

    if request.method == 'POST':
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        section = request.POST.get('section')
        semester = request.POST.get('semester')
        subject_name = request.POST.get('subject_name')
        exam_year = request.POST.get('exam_year')
        question_paper = request.FILES.get('question_paper')

        if not subject_name or not exam_year or not question_paper:
            return render(
                request,
                'portal/upload_question_paper.html',
                {'message': '❌ Please fill all fields and select a PDF.'}
            )

        QuestionPaper.objects.create(
            faculty=request.user.faculty,
            branch=branch,
            year=year,
            section=section,
            semester=semester,
            subject_name=subject_name,
            exam_year=exam_year,
            question_paper=question_paper
        )

        return render(
            request,
            'portal/upload_question_paper.html',
            {'message': '✅ Question paper uploaded successfully!'}
        )

    return render(request, 'portal/upload_question_paper.html')
def question_papers(request):
    branch = request.session.get('branch')
    year = request.session.get('year')
    section = request.session.get('section')
    semester = request.session.get('semester')

    papers = QuestionPaper.objects.filter(
        branch=branch,
        year=year,
        section=section,
        semester=semester
    ).order_by('-exam_year', 'subject_name')

    return render(
        request,
        'portal/question_papers.html',
        {'papers': papers}
    )
   