# Generated by Django 4.2.3 on 2023-08-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_alter_comentario_autor_alter_publicaciones_creador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
