# Generated by Django 4.0.2 on 2022-02-15 08:53

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=5)),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
    ]
