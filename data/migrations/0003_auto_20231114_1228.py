# Generated by Django 3.2.16 on 2023-11-14 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_doctor_healthworker_medicinesupply_nurse_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='prescribed_drug',
            new_name='prescribed_medicine',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='healthworker',
            name='user',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='prescription',
            name='prescribed_by',
            field=models.ForeignKey(default='No doctor available', on_delete=django.db.models.deletion.CASCADE, to='data.doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(choices=[('Santo Rosario', 'Santo Rosario'), ('San Carlos', 'San Carlos'), ('Parian', 'Parian'), ('Balas', 'Balas'), ('Divisoria', 'Divisoria'), ('San Vicente', 'San Vicente'), ('Santo Cristo', 'Santo Cristo'), ('Lagundi', 'Lagundi'), ('San Jose Matulid', 'San Jose Matulid'), ('San Miguel', 'San Miguel'), ('Sabanilla', 'Sabanilla')], max_length=100),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
