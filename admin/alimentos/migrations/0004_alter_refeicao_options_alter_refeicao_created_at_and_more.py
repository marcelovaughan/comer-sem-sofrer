# Generated by Django 4.2 on 2023-05-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0003_refeicao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refeicao',
            options={'verbose_name_plural': 'Refeições'},
        ),
        migrations.AlterField(
            model_name='refeicao',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='refeicao',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
