# Generated by Django 3.2.20 on 2023-07-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('signature', models.CharField(default='It is tender and delicious', max_length=140)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
