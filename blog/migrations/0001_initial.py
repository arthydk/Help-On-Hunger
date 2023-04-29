# Generated by Django 4.1.6 on 2023-02-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, max_length=3000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='image/')),
                ('author', models.CharField(max_length=300)),
            ],
        ),
    ]
