# Generated by Django 3.1.7 on 2021-03-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0006_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
