# Generated by Django 5.0.4 on 2024-05-02 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_course_name_alter_course_preview'),
        ('users', '0003_subscribtion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribtion',
            new_name='Subscription',
        ),
    ]
