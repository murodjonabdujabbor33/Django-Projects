# Generated by Django 4.1.3 on 2022-11-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=60)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=18)),
                ('course_type', models.CharField(max_length=50)),
            ],
        ),
    ]