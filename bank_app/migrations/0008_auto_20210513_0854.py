# Generated by Django 3.2 on 2021-05-13 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank_app', '0007_ledger_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('Bank Account', 'Bank Account'), ('Loan', 'Loan'), ('Foreign Bank Account ', 'Foreign Bank Account')], default='Bank Account', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ExternalLedger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreignAccount', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('text', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('localAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_ledger', to='bank_app.account')),
            ],
        ),
    ]
