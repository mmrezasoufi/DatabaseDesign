# Generated by Django 4.2 on 2024-01-19 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personels', '0003_alter_performancereview_personel_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('establisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_owner', to='personels.personel')),
            ],
            options={
                'verbose_name': 'meeting',
                'verbose_name_plural': 'meetings',
            },
        ),
        migrations.CreateModel(
            name='PersonelsMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personels_meeting', to='interview_meeting.meeting')),
                ('personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_meetings', to='personels.personel')),
            ],
            options={
                'verbose_name': 'personel meeting',
                'verbose_name_plural': 'personels meeting',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.PositiveSmallIntegerField(default=0)),
                ('interview_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('applier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to=settings.AUTH_USER_MODEL)),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='personels.personel')),
            ],
            options={
                'verbose_name': 'interview',
                'verbose_name_plural': 'interviews',
            },
        ),
    ]