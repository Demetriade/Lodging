# Generated by Django 3.0.6 on 2020-05-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodgment', '0003_auto_20200513_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='image',
            field=models.ImageField(default='default_lodge_pic.jpg', upload_to='lodgment_pics'),
        ),
    ]