# Generated by Django 3.2.18 on 2023-03-25 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0021_auto_20230323_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scriptversion',
            options={'permissions': [('download_unsupported_json', 'Can the request the download of a JSON that replaces unsupported characters')]},
        ),
    ]
