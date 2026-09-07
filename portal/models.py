from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
    ]

    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    subject_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    coordinator = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.subject_name


class Timetable(models.Model):
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
    ]

    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    room_no = models.CharField(max_length=20)
    timetable_file = models.FileField(upload_to='timetables/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.branch} - {self.year} Year - {self.section} - {self.semester} Sem"


class Notes(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
    ]

    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
    ]

    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    branch = models.CharField(
        max_length=20,
        choices=BRANCH_CHOICES,
        blank=True,
        null=True
    )

    year = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES,
        blank=True,
        null=True
    )

    section = models.CharField(
        max_length=1,
        choices=SECTION_CHOICES,
        blank=True,
        null=True
    )

    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES,
        blank=True,
        null=True
    )

    subject_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    notes_pdf = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject_name} - {self.branch} - Year {self.year} - {self.section}"


class QuestionPaper(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
    ]

    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
    ]

    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE
    )

    branch = models.CharField(
        max_length=20,
        choices=BRANCH_CHOICES
    )

    year = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES
    )

    section = models.CharField(
        max_length=1,
        choices=SECTION_CHOICES
    )

    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES
    )

    subject_name = models.CharField(
        max_length=100
    )

    exam_year = models.CharField(
        max_length=4
    )

    question_paper = models.FileField(
        upload_to='question_papers/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.subject_name} - {self.exam_year}"