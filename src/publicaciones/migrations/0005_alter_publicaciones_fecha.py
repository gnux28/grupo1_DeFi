# Generated by Django 4.2.3 on 2023-08-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_rename_username_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]