# Generated by Django 5.0.7 on 2024-07-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('photo1', models.ImageField(upload_to='articles/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
