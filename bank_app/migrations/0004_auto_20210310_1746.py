# Generated by Django 3.1.7 on 2021-03-10 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0003_auto_20210309_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='id_account_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledger', to='bank_app.account'),
        ),
    ]
