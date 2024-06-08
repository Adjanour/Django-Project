# Generated by Django 5.0.6 on 2024-06-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transcripts", "0003_alter_transcriptrequest_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="transcriptrequest",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("PAID", "Paid"),
                    ("FAILED", "Failed"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="transcriptrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("PROCESSING", "Processing"),
                    ("COMPLETED", "Completed"),
                    ("REJECTED", "Rejected"),
                    ("CANCELLED", "Cancelled"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
    ]