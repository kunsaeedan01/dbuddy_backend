# Generated by Django 4.0 on 2023-04-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0010_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Coordinator'), ('1', 'Instructor'), ('2', 'Student')], default='2', max_length=10, null=True, verbose_name='Role status'),
        ),
    ]