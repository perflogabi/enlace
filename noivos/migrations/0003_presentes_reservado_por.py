# Generated by Django 4.2.16 on 2024-11-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0002_convidados'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentes',
            name='reservado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noivos.convidados'),
        ),
    ]