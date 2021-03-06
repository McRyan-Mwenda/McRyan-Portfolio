# Generated by Django 4.0.3 on 2022-04-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=2225)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_description',
        ),
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.ManyToManyField(blank=True, to='core.kindword'),
        ),
    ]
