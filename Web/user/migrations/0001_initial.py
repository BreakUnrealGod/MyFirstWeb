# Generated by Django 2.0 on 2019-05-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(default='student@126.com', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]