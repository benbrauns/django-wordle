# Generated by Django 4.0.1 on 2022-01-18 02:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead9df01-feb9-4705-ad11-9dfb32e8c2ff'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8cdda26e-d352-4ab8-a52a-321ae74a564d'), editable=False, primary_key=True, serialize=False),
        ),
    ]