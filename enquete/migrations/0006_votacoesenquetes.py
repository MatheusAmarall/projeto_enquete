# Generated by Django 4.2.8 on 2023-12-05 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enquete', '0005_delete_votacoesenquetes'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotacoesEnquetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquete.enquetes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VotacaoEnquete',
                'verbose_name_plural': 'VotacoesEnquetes',
            },
        ),
    ]