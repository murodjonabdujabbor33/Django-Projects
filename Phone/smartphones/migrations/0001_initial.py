# Generated by Django 4.1.3 on 2022-11-12 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartphones.brand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartphones.model')),
            ],
        ),
    ]