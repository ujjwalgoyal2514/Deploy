# Generated by Django 2.1 on 2023-09-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StuResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('responsetype', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=500)),
                ('responseText', models.CharField(max_length=1000)),
                ('responsedate', models.CharField(max_length=30)),
            ],
        ),
    ]
