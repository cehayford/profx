# Generated by Django 5.1.4 on 2025-01-14 11:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
