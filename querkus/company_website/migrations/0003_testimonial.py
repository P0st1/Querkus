# Generated by Django 5.0.4 on 2024-05-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_website', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=5)),
                ('quote', models.TextField()),
            ],
        ),
    ]
