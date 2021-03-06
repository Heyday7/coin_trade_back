# Generated by Django 3.2.3 on 2021-05-21 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_account_balance'),
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='acc_trade_value',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='acc_trade_value_24H',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='closing_price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='date',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='fluctate_24H',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='fluctate_rate_24H',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='max_price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='min_price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='opening_price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='prev_closing_price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='units_traded',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='units_traded_24H',
        ),
        migrations.AddField(
            model_name='coin',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='coin',
            name='ticker',
            field=models.CharField(default='BTC', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='CoinPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_price', models.FloatField()),
                ('closing_price', models.FloatField()),
                ('min_price', models.FloatField()),
                ('max_price', models.FloatField()),
                ('units_traded', models.FloatField()),
                ('acc_trade_value', models.FloatField()),
                ('prev_closing_price', models.FloatField()),
                ('units_traded_24H', models.FloatField()),
                ('acc_trade_value_24H', models.FloatField()),
                ('fluctate_24H', models.FloatField()),
                ('fluctate_rate_24H', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin.coin')),
            ],
        ),
        migrations.CreateModel(
            name='CoinHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('holding_amount', models.FloatField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coinholdings', related_query_name='coinholding', to='account.account')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin.coin')),
            ],
        ),
    ]
