# Generated by Django 3.0.4 on 2020-05-06 07:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_auto_20200505_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='svg_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]