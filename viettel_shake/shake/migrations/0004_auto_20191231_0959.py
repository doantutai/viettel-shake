# Generated by Django 2.2.9 on 2019-12-31 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shake', '0003_shake_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shake',
            options={'ordering': ('-created_at',)},
        ),
    ]
