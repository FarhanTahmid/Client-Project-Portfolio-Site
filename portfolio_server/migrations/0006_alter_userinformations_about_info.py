# Generated by Django 4.2.2 on 2023-06-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0005_alter_userinformations_about_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformations',
            name='about_info',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]