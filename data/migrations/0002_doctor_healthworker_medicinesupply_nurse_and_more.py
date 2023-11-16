# Generated by Django 4.2.6 on 2023-11-13 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(choices=[('Santo Rosario', 'Santo Rosario'), ('San Carlos', 'San Carlos'), ('Parian', 'Parian'), ('Balas', 'Balas'), ('Divisoria', 'Divisoria'), ('San Vicente', 'San Vicente'), ('Santo Cristo', 'Santo Cristo'), ('Lagundi', 'Lagundi'), ('San Jose Matulid', 'San Jose Matulid'), ('San Miguel', 'San Miguel'), ('Sabanilla', 'Sabanilla')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HealthWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(choices=[('Santo Rosario', 'Santo Rosario'), ('San Carlos', 'San Carlos'), ('Parian', 'Parian'), ('Balas', 'Balas'), ('Divisoria', 'Divisoria'), ('San Vicente', 'San Vicente'), ('Santo Cristo', 'Santo Cristo'), ('Lagundi', 'Lagundi'), ('San Jose Matulid', 'San Jose Matulid'), ('San Miguel', 'San Miguel'), ('Sabanilla', 'Sabanilla')], max_length=200)),
                ('employment_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_code', models.CharField(max_length=200)),
                ('drug_name', models.CharField(max_length=500)),
                ('supply_unit', models.CharField(max_length=300)),
                ('quantity', models.FloatField()),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(choices=[('Santo Rosario', 'Santo Rosario'), ('San Carlos', 'San Carlos'), ('Parian', 'Parian'), ('Balas', 'Balas'), ('Divisoria', 'Divisoria'), ('San Vicente', 'San Vicente'), ('Santo Cristo', 'Santo Cristo'), ('Lagundi', 'Lagundi'), ('San Jose Matulid', 'San Jose Matulid'), ('San Miguel', 'San Miguel'), ('Sabanilla', 'Sabanilla')], max_length=200)),
                ('employment_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.RenameField(
            model_name='healthhistory',
            old_name='history',
            new_name='history_checkup',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.AddField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(default='No diagnosis yet', max_length=200),
        ),
        migrations.AddField(
            model_name='patient',
            name='health_history',
            field=models.CharField(default='No history yet', max_length=200),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='prescribed_drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.medicinesupply'),
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
    ]