# Generated by Django 4.2.3 on 2023-07-13 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0008_surveyinfo_istrain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to=settings.AUTH_USER_MODEL),
        ),
    ]