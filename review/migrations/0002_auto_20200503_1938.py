# Generated by Django 3.0.5 on 2020-05-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(),
        ),
    ]