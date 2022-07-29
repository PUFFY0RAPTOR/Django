# Generated by Django 4.0.6 on 2022-07-29 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aprendiz',
            name='id',
        ),
        migrations.AlterField(
            model_name='aprendiz',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aprendiz',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Monitoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_final', models.DateTimeField()),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='territorio.aprendiz')),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad_realizada', models.CharField(max_length=254)),
                ('obs', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('monitoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='territorio.monitoria')),
            ],
        ),
    ]
