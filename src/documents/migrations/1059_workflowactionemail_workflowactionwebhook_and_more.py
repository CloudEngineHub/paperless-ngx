# Generated by Django 5.1.3 on 2024-11-26 04:07

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1058_workflowtrigger_schedule_date_custom_field_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowActionEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="The subject of the email, can include some placeholders, see documentation.",
                        max_length=256,
                        verbose_name="email subject",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="The body (message) of the email, can include some placeholders, see documentation.",
                        verbose_name="email body",
                    ),
                ),
                (
                    "to",
                    models.TextField(
                        help_text="The destination email addresses, comma separated.",
                        verbose_name="emails to",
                    ),
                ),
                (
                    "include_document",
                    models.BooleanField(
                        default=False,
                        verbose_name="include document in email",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkflowActionWebhook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The destination URL for the notification.",
                        verbose_name="webhook url",
                    ),
                ),
                (
                    "use_params",
                    models.BooleanField(default=True, verbose_name="use parameters"),
                ),
                (
                    "params",
                    models.JSONField(
                        blank=True,
                        help_text="The parameters to send with the webhook URL if body not used.",
                        null=True,
                        verbose_name="webhook parameters",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        blank=True,
                        help_text="The body to send with the webhook URL if parameters not used.",
                        null=True,
                        verbose_name="webhook body",
                    ),
                ),
                (
                    "headers",
                    models.JSONField(
                        blank=True,
                        help_text="The headers to send with the webhook URL.",
                        null=True,
                        verbose_name="webhook headers",
                    ),
                ),
                (
                    "include_document",
                    models.BooleanField(
                        default=False,
                        verbose_name="include document in webhook",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="workflowaction",
            name="type",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Assignment"),
                    (2, "Removal"),
                    (3, "Email"),
                    (4, "Webhook"),
                ],
                default=1,
                verbose_name="Workflow Action Type",
            ),
        ),
        migrations.AddField(
            model_name="workflowaction",
            name="email",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="action",
                to="documents.workflowactionemail",
                verbose_name="email",
            ),
        ),
        migrations.AddField(
            model_name="workflowaction",
            name="webhook",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="action",
                to="documents.workflowactionwebhook",
                verbose_name="webhook",
            ),
        ),
    ]
