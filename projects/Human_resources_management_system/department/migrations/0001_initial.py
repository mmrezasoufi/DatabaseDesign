from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("personels", "0003_alter_performancereview_personel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=45, null=True)),
                ("zone", models.IntegerField(default=0)),
                ("address", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "building",
                "verbose_name_plural": "buildings",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=45, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "director",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departments",
                        to="personels.personel",
                    ),
                ),
            ],
            options={
                "verbose_name": "department",
                "verbose_name_plural": "departments",
            },
        ),
        migrations.CreateModel(
            name="BuildingDepartment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "building",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="building_department",
                        to="department.building",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="building_department",
                        to="department.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "building department",
                "verbose_name_plural": "building departments",
            },
        ),
    ]
