# Generated by Django 3.2 on 2021-05-19 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informatics_server', '0003_repo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('issue', models.TextField()),
                ('is_public', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informatics_server.teammember')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informatics_server.team')),
            ],
        ),
    ]
