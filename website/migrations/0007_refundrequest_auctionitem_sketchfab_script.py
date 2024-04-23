# Generated by Django 4.2.6 on 2024-04-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auctionitem_floor_count_auctionitem_house_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefundRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('bank_branch', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='sketchfab_script',
            field=models.TextField(blank=True, null=True),
        ),
    ]
