# Generated by Django 2.2 on 2019-04-21 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('prefix', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, max_length=300, null=True)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Context')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=60)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Context')),
            ],
        ),
        migrations.CreateModel(
            name='Predicate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Key')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=300, null=True)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Key')),
                ('predicate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Predicate')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledgeHandler.Subject')),
            ],
        ),
    ]
