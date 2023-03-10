# Generated by Django 4.1.5 on 2023-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0004_alter_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Polygender', 'P'), ('Genderfluid', 'G'), ('Agender', 'A'), ('Bigender', 'B')], db_column='gender', max_length=11),
        ),
    ]
