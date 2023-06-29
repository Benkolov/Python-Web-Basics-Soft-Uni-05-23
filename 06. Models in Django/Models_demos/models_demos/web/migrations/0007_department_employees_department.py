# Generated by Django 4.2.1 on 2023-06-08 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_employees_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.department'),
        ),
    ]
