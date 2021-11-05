# Generated by Django 3.2.7 on 2021-11-05 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start1', '0012_auto_20211027_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workunit',
            name='code',
        ),
        migrations.AlterField(
            model_name='inherentrisk',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start1.objective'),
        ),
        migrations.AlterField(
            model_name='inherentrisk',
            name='target_Completion',
            field=models.DateField(blank=True, max_length=300),
        ),
    ]
