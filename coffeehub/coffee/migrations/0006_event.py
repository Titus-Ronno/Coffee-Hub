# Generated by Django 5.0.6 on 2024-06-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_trainingsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
