# Generated by Django 2.2 on 2019-04-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoBeca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('requisito', models.TextField(blank=True, null=True)),
                ('duracion', models.CharField(max_length=50)),
                ('contactos', models.TextField(blank=True, null=True)),
                ('tipo_beca', models.ManyToManyField(to='becas.TipoBeca')),
            ],
        ),
    ]
