# Generated by Django 3.0.8 on 2020-07-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='User',
            new_name='user',
        ),
    ]
