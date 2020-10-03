# Generated by Django 3.0.5 on 2020-10-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KitProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=30)),
                ('cost', models.FloatField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=200)),
                ('kit_sku', models.CharField(max_length=30)),
                ('products', models.ManyToManyField(to='api.KitProducts')),
            ],
        ),
    ]
