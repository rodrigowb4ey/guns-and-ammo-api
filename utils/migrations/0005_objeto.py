# Generated by Django 4.0.4 on 2022-05-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0004_objetotipo_alter_calibre_desc_calibre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto_tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utils.objetotipo')),
            ],
        ),
    ]