# Generated by Django 2.0.10 on 2019-01-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190111_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapitreclasse',
            name='idChapitreClasse',
        ),
        migrations.AddField(
            model_name='chapitreclasse',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
