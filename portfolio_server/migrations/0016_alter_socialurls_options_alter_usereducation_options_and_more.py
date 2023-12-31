# Generated by Django 4.2.2 on 2023-06-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0015_userskills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialurls',
            options={'verbose_name': 'User Socials Url'},
        ),
        migrations.AlterModelOptions(
            name='usereducation',
            options={'verbose_name': 'User Education Detail'},
        ),
        migrations.AlterModelOptions(
            name='userinformations',
            options={'verbose_name': 'User Detail'},
        ),
        migrations.AlterModelOptions(
            name='userskills',
            options={'verbose_name': 'User Skill'},
        ),
        migrations.AlterModelOptions(
            name='wavinglines',
            options={'verbose_name': 'Tag Line'},
        ),
        migrations.AddField(
            model_name='userskills',
            name='skill_weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='skill_description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
