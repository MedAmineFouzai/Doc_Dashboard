# Generated by Django 3.0.7 on 2020-06-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_document_app', '0006_auto_20200630_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famille',
            name='famille_id',
            field=models.IntegerField(max_length=100, primary_key=True, serialize=False),
        ),
    ]