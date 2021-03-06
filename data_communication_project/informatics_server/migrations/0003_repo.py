# Generated by Django 3.2 on 2021-05-19 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informatics_server', '0002_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloadToken1', models.TextField()),
                ('downloadToken2', models.TextField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informatics_server.team')),
            ],
        ),
    ]
