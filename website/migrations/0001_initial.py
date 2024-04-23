# Generated by Django 4.2.6 on 2024-03-04 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_bid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='auction_item_images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
