# Generated by Django 4.0.5 on 2022-10-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopeazy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]