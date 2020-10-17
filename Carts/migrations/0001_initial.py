# Generated by Django 3.0.3 on 2020-05-25 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acubook', '0008_auto_20200510_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('currentuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acubook.UserProfileInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acubook.BookInfo')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carts.Cart')),
            ],
        ),
    ]
