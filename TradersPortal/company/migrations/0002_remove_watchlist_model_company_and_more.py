# Generated by Django 5.0.6 on 2024-06-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist_model',
            name='company',
        ),
        migrations.AddField(
            model_name='watchlist_model',
            name='company_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='watchlist_model',
            name='scripcode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='watchlist_model',
            name='symbol',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
