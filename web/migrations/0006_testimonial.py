# Generated by Django 4.1.2 on 2022-10-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_videoblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('logo', models.FileField(upload_to='document/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('isfeatured', models.BooleanField(default=False)),
            ],
        ),
    ]
