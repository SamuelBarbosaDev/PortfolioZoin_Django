# Generated by Django 4.1.1 on 2022-10-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_portfolio_portfoliocategoria_portfolioimagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('data_de_criação', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação')),
            ],
        ),
        migrations.CreateModel(
            name='ContatoRedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rede_social', models.CharField(blank=True, choices=[('twitter', 'twitter'), ('instagram', 'instagram'), ('whatsapp', 'whatsapp'), ('telegram', 'telegram'), ('behance', 'behance'), ('twitch', 'twitch'), ('github', 'github'), ('linkedin', 'linkedin'), ('reddit', 'reddit'), ('diagram-2-fill', 'diagram-2-fill')], default='diagram-2-fill', max_length=50, null=True)),
                ('url', models.CharField(blank=True, default='https://www.instagram.com/samuelbarbosa_dev/', max_length=500, null=True)),
                ('add_redeSocial', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contato')),
            ],
        ),
    ]
