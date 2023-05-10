# Generated by Django 4.1.7 on 2023-05-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=100)),
                ('smobile', models.CharField(max_length=10)),
                ('saddress', models.CharField(max_length=255)),
                ('scollege', models.CharField(max_length=255)),
                ('sdegree', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('due_amount', models.FloatField()),
            ],
        ),
    ]