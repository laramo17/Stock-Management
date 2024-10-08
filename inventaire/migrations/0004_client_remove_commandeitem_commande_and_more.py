# Generated by Django 5.0.6 on 2024-06-28 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0003_commandeitem_prix_vente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('idCl', models.AutoField(primary_key=True, serialize=False)),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='commandeitem',
            name='commande',
        ),
        migrations.RemoveField(
            model_name='commandeitem',
            name='produit',
        ),
        migrations.CreateModel(
            name='CommandeProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField()),
                ('prix_vente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventaire.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventaire.produit')),
            ],
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
        migrations.DeleteModel(
            name='CommandeItem',
        ),
    ]
