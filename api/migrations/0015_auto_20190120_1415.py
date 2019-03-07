# Generated by Django 2.0.10 on 2019-01-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_question_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='contenuFichier',
            field=models.FileField(blank=True, null=True, upload_to='chapitre/fichier/'),
        ),
        migrations.AddField(
            model_name='section',
            name='contenuVideo',
            field=models.FileField(blank=True, null=True, upload_to='chapitre/video/'),
        ),
    ]