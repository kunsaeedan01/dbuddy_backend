# Generated by Django 4.0 on 2023-04-03 05:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_user', '0006_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='Project Title', max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('WA', 'Web-application'), ('MA', 'Mobile application'), ('GM', 'Game'), ('HW', 'Hardware'), ('MD', 'Media'), ('NN', 'Neural Network'), ('RT', 'Research')], max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_user.user')),
                ('participant1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant1', to='core_user.user')),
                ('participant2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant2', to='core_user.user')),
                ('participant3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant3', to='core_user.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
