# Generated by Django 4.2.2 on 2023-06-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0007_alter_usereducation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformations',
            name='interest',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
