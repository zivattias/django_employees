# Generated by Django 4.1.5 on 2023-01-29 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(db_column='company_name', max_length=256)),
                ('country', models.CharField(db_column='country', max_length=128)),
                ('city', models.CharField(db_column='city', max_length=128)),
                ('address', models.CharField(db_column='address', max_length=128)),
                ('phone_num', models.CharField(db_column='phone_num', max_length=128)),
            ],
            options={
                'db_table': 'comapnies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_column='firstname', max_length=128)),
                ('lastname', models.CharField(db_column='lastname', max_length=128)),
                ('personal_email', models.EmailField(db_column='personal_email', max_length=256)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], db_column='gender', max_length=6)),
                ('birth_date', models.DateField(db_column='birth_date')),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(db_column='job_title', max_length=256)),
                ('is_current_job', models.BooleanField(db_column='is_current_job')),
                ('employee_email', models.EmailField(db_column='employee_email', max_length=254, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees_app.company')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees_app.person')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(through='employees_app.Employee', to='employees_app.person'),
        ),
    ]
