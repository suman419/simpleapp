# Generated by Django 2.1 on 2018-12-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='simage',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
