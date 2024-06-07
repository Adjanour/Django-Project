# Generated by Django 5.0.6 on 2024-06-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0013_remove_studentprofile_verification_document"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentprofile",
            name="graduation_year",
        ),
        migrations.RemoveField(
            model_name="studentprofile",
            name="student_id",
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="profile_image",
            field=models.ImageField(upload_to="profile_images/"),
        ),
    ]