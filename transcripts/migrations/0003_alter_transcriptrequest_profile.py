# Generated by Django 5.0.6 on 2024-05-27 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_studentprofile_verification_status"),
        ("transcripts", "0002_transcriptrequest_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transcriptrequest",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="accounts.studentprofile",
            ),
        ),
    ]