# Generated by Django 3.0.6 on 2020-06-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinashe_projects', '0003_auto_20200606_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='staticfiles/about'),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='image',
            field=models.ImageField(upload_to='staticfiles/works'),
        ),
    ]