# Generated by Django 5.0.6 on 2024-05-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]
