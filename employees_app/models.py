from django.db import models


class Company(models.Model):
    company_name = models.CharField(db_column='company_name', max_length=256, null=False, blank=False)
    country = models.CharField(db_column='country', max_length=128, null=False, blank=False)
    city = models.CharField(db_column='city', max_length=128, null=False, blank=False)
    address = models.CharField(db_column='address', max_length=128, null=False, blank=False)
    phone_num = models.CharField(db_column='phone_num', max_length=128, null=False, blank=False)
    employees = models.ManyToManyField(to='Person', through='Employee')

    class Meta:
        db_table = 'companies'


class Employee(models.Model):
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    job_title = models.CharField(db_column='job_title', max_length=256, null=False, blank=False)
    is_current_job = models.BooleanField(db_column='is_current_job', null=False, blank=False)
    employee_email = models.EmailField(db_column='employee_email', null=True, blank=False)

    class Meta:
        db_table = 'employees'


class Person(models.Model):
    first_name = models.CharField(db_column='first_name', max_length=128, null=False, blank=False)
    last_name = models.CharField(db_column='last_name', max_length=128, null=False, blank=False)
    personal_email = models.EmailField(db_column='personal_email', max_length=256, null=False, blank=False)
    gender = models.CharField(db_column='gender', max_length=11, choices=[('Male', 'M'), ('Female', 'F'), ('Polygender', 'P'), ('Genderfluid', 'G'), ('Agender', 'A'), ('Bigender', 'B')], null=False, blank=False)
    birth_date = models.DateField(db_column='birth_date', null=False, blank=False)

    class Meta:
        db_table = 'persons'