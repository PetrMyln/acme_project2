# Generated by Django 3.2.16 on 2024-10-05 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birthdays', to=settings.AUTH_USER_MODEL, verbose_name='Автор записи'),
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birthday'), name='Unique person constraint'),
        ),
    ]
