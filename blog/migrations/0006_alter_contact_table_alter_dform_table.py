# Generated by Django 4.1.6 on 2023-03-08 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_contacts_contact_alter_contact_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contact',
            table='contacts',
        ),
        migrations.AlterModelTable(
            name='dform',
            table='donates',
        ),
    ]
