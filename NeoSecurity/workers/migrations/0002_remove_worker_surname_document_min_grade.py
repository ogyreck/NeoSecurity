# Generated by Django 4.2.10 on 2024-03-15 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='surname',
        ),
        migrations.AddField(
            model_name='document',
            name='min_grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='workers.grade'),
            preserve_default=False,
        ),
    ]
