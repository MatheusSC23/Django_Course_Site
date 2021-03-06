# Generated by Django 3.2.8 on 2021-10-14 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_auto_20211013_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participant'),
        ),
    ]
