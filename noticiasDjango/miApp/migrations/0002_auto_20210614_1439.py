# Generated by Django 3.2.3 on 2021-06-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='numeroNoticia',
        ),
        migrations.AddField(
            model_name='noticias',
            name='imagenNoticia',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]