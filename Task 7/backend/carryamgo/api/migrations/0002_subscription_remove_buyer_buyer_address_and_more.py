# Generated by Django 4.2.2 on 2023-06-15 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcription_type', models.CharField(choices=[('basic', 'Basic'), ('professional', 'Professional')], default='basic', max_length=20)),
                ('subscription_amount', models.IntegerField(choices=[(5000, '5000'), (9000, '9000')], default=5000)),
                ('subscription_description', models.CharField(default='The best way to get started with our services', max_length=255)),
                ('subscription_inventory', models.IntegerField(choices=[(100, 100), (300, 300)], default=100)),
                ('duration', models.DurationField(default='30 days')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='buyer_address',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='product',
        ),
        migrations.AddField(
            model_name='buyer',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('order', 'New Order'), ('promotion', 'New Promotion'), ('end_promotion', 'End of Promotion'), ('message', 'New Message'), ('shop', 'New Shop'), ('product', 'New Product')], default='order', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.seller'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.shop'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='promotion_image',
            field=models.ImageField(default='promotion image', upload_to='promotion images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='name_market',
            field=models.CharField(default='muea market', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='buyer_password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.buyer'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.seller'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='Product Image'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
