# Generated by Django 3.0.3 on 2020-03-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_key_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='type',
            field=models.CharField(choices=[('SSH', 'SSH'), ('FTB', 'FTB'), ('ADMIN', 'ADMIN'), ('EMAIL', 'EMAIL')], default='SSH', max_length=255),
        ),
    ]
