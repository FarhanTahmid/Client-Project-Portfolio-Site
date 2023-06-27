# Generated by Django 4.2.2 on 2023-06-27 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformations',
            name='banner_picture',
            field=models.ImageField(null=True, upload_to='banner_pictures/'),
        ),
        migrations.AddField(
            model_name='userinformations',
            name='nationality',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='userEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=50)),
                ('institutions', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_server.userinformations')),
            ],
            options={
                'verbose_name': 'User Education Details',
            },
        ),
    ]
