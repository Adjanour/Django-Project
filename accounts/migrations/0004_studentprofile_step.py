# Generated by Django 5.0.6 on 2024-05-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentprofile",
            name="step",
            field=models.IntegerField(default=1),
        ),
    ]