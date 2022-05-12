# Generated by Django 3.2.8 on 2022-05-02 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Қолданушы жайныда', 'verbose_name_plural': 'Қолданушылар жайныда'},
        ),
        migrations.AddField(
            model_name='customer',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teacher_students', to=settings.AUTH_USER_MODEL, verbose_name='Мұғалім оқушылары'),
        ),
    ]