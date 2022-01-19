# Generated by Django 4.0.1 on 2022-01-18 02:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0002_alter_game_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(default=uuid.UUID('252c00b5-78f4-4600-a28d-dded2451145c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3c6b8bed-92f5-4d72-b3e6-046d2c1eee27'), editable=False, primary_key=True, serialize=False),
        ),
    ]