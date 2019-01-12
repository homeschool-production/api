# Generated by Django 2.0.10 on 2019-01-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_enseigneaclasse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapitreclasse',
            name='contenu',
        ),
        migrations.RemoveField(
            model_name='chapitreclasse',
            name='id',
        ),
        migrations.AddField(
            model_name='chapitreclasse',
            name='contenuFichier',
            field=models.FileField(blank=True, null=True, upload_to='chapitre/fichier/'),
        ),
        migrations.AddField(
            model_name='chapitreclasse',
            name='contenuVideo',
            field=models.FileField(blank=True, null=True, upload_to='chapitre/video/'),
        ),
        migrations.AddField(
            model_name='chapitreclasse',
            name='idChapitreClasse',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapitreclasse',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]