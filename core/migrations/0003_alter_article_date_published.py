# Generated by Django 4.0.3 on 2022-03-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_article_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
