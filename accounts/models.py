# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    # add additional fields in here
    # profile = models.OneToOneField('StudentProfile', on_delete=models.CASCADE, null=True, blank=True)
    pass


class IdentificationType(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True
    )


class Programme(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True
    )


class GraduateType(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True
    )


class StudentProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.PROTECT, null=False, blank=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    other_names = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(default="1990-02-22")
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True, blank=False)
    postal_address = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255, blank=False)
    profile_image = models.ImageField(upload_to="profile_images/", blank=False)
    identification_file = models.FileField(
        upload_to="identification_documents/", blank=False
    )
    identification_type = models.ForeignKey(
        IdentificationType, on_delete=models.PROTECT, null=True, blank=False
    )
    identification_number = models.CharField(max_length=30, blank=False, null=True)
    step = models.IntegerField(default=1)
    verification_status = models.CharField(
        max_length=20,
        choices=(
            ("NOT SUBMITED", "Not Submited"),
            ("PENDING", "Pending"),
            ("VERIFIED", "Verified"),
            ("REJECTED", "Rejected"),
        ),
        default="NOT SUBMITED",
    )


class CourseLog(models.Model):
    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    graduate_type = models.ForeignKey(GraduateType, on_delete=models.PROTECT)
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    admission_year = models.PositiveIntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2050)]
    )
    graduation_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(2000), MaxValueValidator(2050)],
    )

    def __str__(self):
        return f"{self.full_name} - {self.programme}"
