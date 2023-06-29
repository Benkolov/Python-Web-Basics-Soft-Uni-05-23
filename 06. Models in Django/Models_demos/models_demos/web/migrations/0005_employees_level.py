# Generated by Django 4.2.1 on 2023-06-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_nullblankdemo_id_nullblankdemo_custom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='level',
            field=models.CharField(choices=[(1, 'Junior'), (2, 'Middle'), (3, 'Senior')], default=1, max_length=10),
        ),
    ]
