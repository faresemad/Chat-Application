# Generated by Django 4.2.7 on 2024-02-05 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="online",
            new_name="members",
        ),
        migrations.AddField(
            model_name="room",
            name="admin",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room_admin",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]