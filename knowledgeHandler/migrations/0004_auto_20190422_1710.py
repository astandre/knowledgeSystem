# Generated by Django 2.2 on 2019-04-22 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgeHandler', '0003_auto_20190422_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='object',
            old_name='subject',
            new_name='object',
        ),
    ]
