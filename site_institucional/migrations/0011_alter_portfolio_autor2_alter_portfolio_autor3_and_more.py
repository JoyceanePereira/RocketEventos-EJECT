# Generated by Django 4.0.6 on 2022-07-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_institucional', '0010_alter_inicio_titulo1_alter_inicio_titulo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='autor2',
            field=models.CharField(default='', max_length=50, verbose_name='Autor 2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='autor3',
            field=models.CharField(default='', max_length=50, verbose_name='Autor 3'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='autor4',
            field=models.CharField(default='', max_length=50, verbose_name='Autor 4'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='comentario2',
            field=models.TextField(default='', max_length=250, verbose_name='Comentario 2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='comentario3',
            field=models.TextField(default='', max_length=250, verbose_name='Comentario 3'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='comentario4',
            field=models.TextField(default='', max_length=250, verbose_name='Comentario 4'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image1',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 1'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 3'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image4',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 4'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image5',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 5'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image6',
            field=models.ImageField(upload_to='fotos', verbose_name='Imagem 6'),
        ),
    ]
