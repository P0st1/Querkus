# Generated by Django 5.0.4 on 2024-05-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_website', '0007_alter_service_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='template',
            field=models.CharField(choices=[('obrezovanje-dreves.html', 'Obrezovanje dreves'), ('podiranje-dreves.html', 'Podiranje dreves'), ('obrezovanje-zive-meje.html', 'Obrezovanje žive meje')], max_length=100),
        ),
    ]
