# Generated by Django 5.0.3 on 2024-04-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='bolg')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]