# Generated by Django 4.2.8 on 2023-12-05 00:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enquete', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enquete',
            new_name='Enquetes',
        ),
        migrations.RenameModel(
            old_name='VotacaoEnquete',
            new_name='VotacoesEnquetes',
        ),
        migrations.AlterModelOptions(
            name='votacoesenquetes',
            options={'verbose_name': 'VotacaoEnquete', 'verbose_name_plural': 'VotacoesEnquetes'},
        ),
    ]
