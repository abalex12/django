# Generated by Django 5.0.7 on 2024-07-14 21:22

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicStatus',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=10, prefix='AcSt', primary_key=True, serialize=False, unique=True)),
                ('status_name', models.CharField(choices=[('enrolled', 'Enrolled'), ('probation', 'Probation'), ('dismissed', 'Dismissed'), ('graduated', 'Graduated')], max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=10, prefix='Cour', primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(db_index=True, max_length=100)),
                ('course_code', models.CharField(db_index=True, max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('credit_hours', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=10, prefix='Dep', primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(db_index=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('office_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enrollment_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=9, max_length=10, prefix='Enro', primary_key=True, serialize=False, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('is_retake', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('section_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=9, max_length=10, prefix='Sec', primary_key=True, serialize=False, unique=True)),
                ('section_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademicRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('record_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=9, max_length=10, prefix='StAc', primary_key=True, serialize=False, unique=True)),
                ('semester_number', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('is_current', models.BooleanField(db_index=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAssignment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=9, max_length=10, prefix='TeAs', primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcademicPeriod',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academic_period_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=10, prefix='AcPe', primary_key=True, serialize=False, unique=True)),
                ('academic_year', models.CharField(db_index=True, max_length=20)),
                ('semester', models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter')], db_index=True, max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'ordering': ['academic_year', 'semester'],
                'indexes': [models.Index(fields=['academic_year', 'semester'], name='Academics_a_academi_272133_idx')],
                'unique_together': {('academic_year', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='CourseDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='Academics.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('offering_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=9, max_length=10, prefix='CoOf', primary_key=True, serialize=False, unique=True)),
                ('academic_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offerings', to='Academics.academicperiod')),
                ('course_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offerings', to='Academics.coursedepartment')),
            ],
        ),
    ]