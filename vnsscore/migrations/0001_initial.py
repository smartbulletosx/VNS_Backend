# Generated by Django 3.1.7 on 2021-03-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('result', models.IntegerField()),
                ('result_race', models.TimeField()),
            ],
        ),
    ]
