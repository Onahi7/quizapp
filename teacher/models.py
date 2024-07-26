from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class ActiveTeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')

class Teacher(models.Model):
    STATUS_CHOICES = [
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('on_leave', _('On Leave')),
    ]

    DEPARTMENT_CHOICES = [
        ('math', _('Mathematics')),
        ('science', _('Science')),
        ('literature', _('Literature')),
        ('history', _('History')),
        ('computer_science', _('Computer Science')),
        ('other', _('Other')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    profile_pic = models.ImageField(
        upload_to='teachers/profile_pics/',
        null=True,
        blank=True,
        help_text=_("Upload a profile picture")
    )
    address = models.CharField(max_length=200, help_text=_("Enter the full address"))
    mobile = models.CharField(
        max_length=20,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        )],
        help_text=_("Enter a valid phone number")
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text=_("Select the current status of the teacher")
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text=_("Enter the salary amount")
    )
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default='other',
        help_text=_("Select the department")
    )
    join_date = models.DateField(help_text=_("Enter the date the teacher joined"))
    bio = models.TextField(blank=True, help_text=_("Enter a brief biography"))

    objects = models.Manager()
    active_teachers = ActiveTeacherManager()

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
        ordering = ['user__last_name', 'user__first_name']

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip()

    def get_courses(self):
        return self.courses.all()  # Assuming there's a related Course model with a ForeignKey to Teacher

    def is_active(self):
        return self.status == 'active'

    def __str__(self):
        return f"{self.get_full_name} - {self.get_department_display()}"

    def save(self, *args, **kwargs):
        self.full_clean()  # This calls validators
        super().save(*args, **kwargs)

# Assuming you have a Course model, it might look something like this:
class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    # ... other fields ...

    def __str__(self):
        return self.name