# Generated by Django 3.2.7 on 2021-10-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start1', '0005_remove_majoractivity_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inherentrisk',
            name='consequence',
        ),
        migrations.RemoveField(
            model_name='inherentrisk',
            name='risk_Level',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_IadUSer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_RmcdUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inherentrisk',
            name='risk_Condition',
            field=models.CharField(blank=True, choices=[('Tolerable', 'Tolerable'), ('Reversible', 'Reversible'), ('costly', 'Costly Reversible'), ('Unreversible', 'Unreversible')], max_length=30),
        ),
    ]
