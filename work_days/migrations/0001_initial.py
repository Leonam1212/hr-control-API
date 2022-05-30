# Generated by Django 4.0.4 on 2022-05-26 18:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checkin', models.DateTimeField(auto_now_add=True)),
                ('checkout', models.DateTimeField(null=True)),
                ('time_worked', models.TimeField(null=True)),
                ('is_holiday', models.BooleanField(default=False)),
                ('is_weekend', models.BooleanField(default=False)),
            ],
        ),
    ]
