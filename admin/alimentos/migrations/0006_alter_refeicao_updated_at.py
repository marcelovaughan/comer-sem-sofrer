# Generated by Django 4.2 on 2023-05-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0005_alter_refeicao_created_at_alter_refeicao_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refeicao',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
