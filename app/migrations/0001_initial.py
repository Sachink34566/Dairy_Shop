# Generated by Django 4.2.5 on 2024-04-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CE', 'Curd'), ('CZ', 'Cheese'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('IC', 'Ice-Creams')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
