# Generated by Django 4.0 on 2023-05-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_project', '0004_tag_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('WA', 'Web-application'), ('MA', 'Mobile application'), ('GM', 'Game'), ('HW', 'Hardware'), ('MD', 'Media'), ('NN', 'Neural Network'), ('RT', 'Research')], max_length=64),
        ),
    ]