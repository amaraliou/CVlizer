# Generated by Django 2.1.4 on 2019-01-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvlizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=255)),
                ('schoolLocation', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('gpa', models.CharField(max_length=100)),
                ('startDate', models.CharField(max_length=50)),
                ('endDate', models.CharField(max_length=50)),
            ],
        ),
    ]
