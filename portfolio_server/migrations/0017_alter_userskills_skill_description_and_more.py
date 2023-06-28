# Generated by Django 4.2.2 on 2023-06-28 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_server', '0016_alter_socialurls_options_alter_usereducation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskills',
            name='skill_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='UserResearchExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_institute', models.CharField(max_length=150)),
                ('research_project', models.CharField(blank=True, max_length=200, null=True)),
                ('project_description', models.TextField(blank=True, max_length=500, null=True)),
                ('project_outcome', models.CharField(max_length=200, null=True)),
                ('research_weight', models.TextField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_server.userinformations')),
            ],
            options={
                'verbose_name': 'User Research Experience',
            },
        ),
    ]