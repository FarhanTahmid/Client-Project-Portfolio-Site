# Generated by Django 4.2.2 on 2023-06-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0010_usereducation_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereducation',
            name='project',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]