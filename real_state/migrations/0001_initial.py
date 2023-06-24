# Generated by Django 3.2 on 2023-05-13 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('transaction_type', models.CharField(choices=[('sale', 'Sale'), ('rent', 'Rent')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('square_meters', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bathrooms', models.PositiveIntegerField()),
                ('bedrooms', models.PositiveIntegerField()),
                ('car_parking', models.PositiveBigIntegerField(default=0)),
                ('main_image', models.ImageField(upload_to='property_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_state.category')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='real_state.property')),
            ],
        ),
    ]