# Generated by Django 2.2 on 2019-04-23 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgeHandler', '0009_auto_20190423_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predicate',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Key'),
        ),
    ]
