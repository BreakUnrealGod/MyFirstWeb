# Generated by Django 2.0 on 2019-05-24 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookname',
        ),
    ]