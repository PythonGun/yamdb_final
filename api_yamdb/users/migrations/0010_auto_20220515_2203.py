# Generated by Django 2.2.16 on 2022-05-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220515_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=5, verbose_name='Код подтверждения'),
        ),
    ]
