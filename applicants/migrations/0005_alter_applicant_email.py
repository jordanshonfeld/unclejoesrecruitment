# Generated by Django 4.0.6 on 2022-08-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0004_writtenapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
