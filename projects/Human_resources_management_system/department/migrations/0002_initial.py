# Generated by Django 4.2 on 2024-02-04 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('personels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='personels.personel'),
        ),
        migrations.AddField(
            model_name='buildingdepartment',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_department', to='department.building'),
        ),
        migrations.AddField(
            model_name='buildingdepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_department', to='department.department'),
        ),
    ]