# Generated by Django 5.0.6 on 2024-05-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_alter_application_driver_delete_driverimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=255, upload_to='store/products')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(max_length=255, upload_to='store/products')),
            ],
        ),
    ]
