# Generated by Django 4.0.4 on 2022-05-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_alter_calibre_id_alter_objeto_id_alter_objetotipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]