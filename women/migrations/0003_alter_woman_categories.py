# Generated by Django 4.2 on 2023-04-06 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_woman_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='women', to='women.category'),
        ),
    ]
