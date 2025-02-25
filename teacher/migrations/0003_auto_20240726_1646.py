# Generated by Django 3.0.5 on 2024-07-26 15:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0002_teacher_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['user__last_name', 'user__first_name'], 'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='bio',
            field=models.TextField(blank=True, help_text='Enter a brief biography'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('math', 'Mathematics'), ('science', 'Science'), ('literature', 'Literature'), ('history', 'History'), ('computer_science', 'Computer Science'), ('other', 'Other')], default='other', help_text='Select the department', max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='join_date',
            field=models.DateField(default=1, help_text='Enter the date the teacher joined'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(help_text='Enter the full address', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.CharField(help_text='Enter a valid phone number', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, help_text='Upload a profile picture', null=True, upload_to='teachers/profile_pics/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter the salary amount', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('on_leave', 'On Leave')], default='active', help_text='Select the current status of the teacher', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='teacher.Teacher')),
            ],
        ),
    ]
