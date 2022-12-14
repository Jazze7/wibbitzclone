# Generated by Django 4.1.2 on 2022-10-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('company_size', models.CharField(choices=[('1', '1-10'), ('2', '11-50'), ('3', '50-100'), ('4', '100-200')], max_length=255)),
                ('industry', models.CharField(choices=[('1', 'Industry'), ('2', 'Agriculture'), ('3', 'Banking & Finance'), ('4', 'Business Services & Software')], max_length=255)),
                ('job', models.CharField(choices=[('1', 'Software Engineer'), ('2', 'Database Engineer'), ('3', 'Business Analytics'), ('4', 'Developer')], max_length=255)),
                ('country', models.CharField(choices=[('1', 'India'), ('2', 'USA'), ('3', 'UK'), ('4', 'UAE')], max_length=255)),
                ('user_agreement', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'web_data',
                'ordering': ['-id'],
            },
        ),
    ]
