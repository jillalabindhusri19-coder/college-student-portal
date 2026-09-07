from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [

        # Faculty: rename faculty_name to name
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='name',
        ),

        # Remove old Faculty fields
        migrations.RemoveField(
            model_name='faculty',
            name='faculty_id',
        ),

        migrations.RemoveField(
            model_name='faculty',
            name='profile_photo',
        ),

        # Remove old Notes subject relationship
        migrations.RemoveField(
            model_name='notes',
            name='subject',
        ),

        # Add Branch to Notes
        migrations.AddField(
            model_name='notes',
            name='branch',
            field=models.CharField(
                blank=True,
                null=True,
                max_length=20,
                choices=[
                    ('CSE', 'CSE'),
                    ('ECE', 'ECE'),
                    ('EEE', 'EEE'),
                    ('MECH', 'MECH'),
                    ('CIVIL', 'CIVIL'),
                ],
            ),
        ),

        # Add Semester to Notes
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.CharField(
                blank=True,
                null=True,
                max_length=1,
                choices=[
                    ('1', '1st Semester'),
                    ('2', '2nd Semester'),
                ],
            ),
        ),

        # Add Subject Name to Notes
        migrations.AddField(
            model_name='notes',
            name='subject_name',
            field=models.CharField(
                blank=True,
                null=True,
                max_length=100,
            ),
        ),

        # Add Year to Notes
        migrations.AddField(
            model_name='notes',
            name='year',
            field=models.CharField(
                blank=True,
                null=True,
                max_length=1,
                choices=[
                    ('1', '1st Year'),
                    ('2', '2nd Year'),
                    ('3', '3rd Year'),
                ],
            ),
        ),

        # Change Notes section
        migrations.AlterField(
            model_name='notes',
            name='section',
            field=models.CharField(
                blank=True,
                null=True,
                max_length=1,
                choices=[
                    ('A', 'A'),
                    ('B', 'B'),
                    ('C', 'C'),
                    ('D', 'D'),
                ],
            ),
        ),

        # Make Subject coordinator optional
        migrations.AlterField(
            model_name='subject',
            name='coordinator',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='portal.faculty',
            ),
        ),
    ]