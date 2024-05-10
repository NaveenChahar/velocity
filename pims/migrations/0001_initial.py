# Generated by Django 2.2.1 on 2024-05-08 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('stock_quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_info', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(max_length=50)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pims.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pims.Supplier'),
        ),
    ]