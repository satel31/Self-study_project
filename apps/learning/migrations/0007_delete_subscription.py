# Generated by Django 4.2.5 on 2023-09-15 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_alter_useranswer_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]