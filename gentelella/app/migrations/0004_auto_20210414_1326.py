# Generated by Django 2.2.6 on 2021-04-14 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_notes_note_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(default='', max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='notes',
            name='unique_condition',
        ),
        migrations.AddConstraint(
            model_name='notes',
            constraint=models.UniqueConstraint(fields=('user', 'scenario', 'workspace', 'wsview'), name='unique_note'),
        ),
        migrations.AddField(
            model_name='patientcase',
            name='scenario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Scenario'),
        ),
        migrations.AddField(
            model_name='patientcase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='patientcase',
            constraint=models.UniqueConstraint(fields=('patient_id', 'timestamp'), name='unique_patientcase'),
        ),
    ]
