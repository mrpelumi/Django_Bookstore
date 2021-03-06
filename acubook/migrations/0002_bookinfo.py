# Generated by Django 3.0.4 on 2020-04-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acubook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=265, unique=True)),
                ('Author', models.CharField(max_length=256)),
                ('Publish_year', models.IntegerField()),
                ('Category', models.CharField(choices=[('Arts and Literature', 'Arts and Literature'), ('Science', 'Science'), ('Christian Books', 'Christian Books'), ('Nigerian and African Authors', 'Nigerian and African Authors'), ('Motivational', 'Motivational'), ('Business', 'Business'), ('Teen Books', 'Teen Books')], max_length=256)),
                ('Price', models.IntegerField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
