# Generated by Django 4.1.2 on 2022-10-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='document/'),
        ),
    ]
