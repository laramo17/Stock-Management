# Generated by Django 5.0.6 on 2024-06-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0002_commande_addresseclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandeitem',
            name='prix_vente',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
