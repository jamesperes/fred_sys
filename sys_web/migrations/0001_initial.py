# Generated by Django 2.0.7 on 2018-08-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternativa1', models.CharField(max_length=20)),
                ('alternativa2', models.CharField(max_length=20)),
                ('alternativa3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterio1', models.CharField(max_length=20)),
                ('criterio2', models.CharField(max_length=20)),
                ('criterio3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Decisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decisor1', models.CharField(max_length=20)),
                ('decisor2', models.CharField(max_length=20)),
                ('decisor3', models.CharField(max_length=20)),
            ],
        ),
    ]
