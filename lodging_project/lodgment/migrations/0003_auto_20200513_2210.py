# Generated by Django 3.0.6 on 2020-05-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0002_auto_20200513_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='lodgment_pics'),
        ),
    ]
