# Generated by Django 4.2.8 on 2023-12-05 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0004_enquetes_enquete_aberta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VotacoesEnquetes',
        ),
    ]
