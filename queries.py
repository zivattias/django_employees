import os
from datetime import datetime
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"
django.setup()

from employees_app.models import *

# Queries:

def get_person_name_by_id(person_id: int) -> str:
    """
    Given person id, return string that represents person full name
    :param person_id:
    :return str (first_name + last_name):
    """
    p = Person.objects.get(id=person_id)
    return f"{p.first_name} {p.last_name}"


def get_people_by_age(age: int) -> list[Person]:
    """
    Given age in years, return list of persons of this age
    :param age:
    :return:
    """
    birth_year = str(datetime.now().year - age)
    return list(Person.objects.filter(birth_date__contains=birth_year))


def get_people_cnt_by_gender(gender: str) -> list[Person]:
    """
    Given the gender, return list of people of this gender
    :param gender:
    :return:
    """
    return list(Person.objects.filter(gender=gender))


def get_companies_by_country(country: str) -> list[str]:
    """
    Given country name, return list of companies' names in this country
    :param country:
    :return:
    """
    return list(Company.objects.filter(country=country))


def get_company_employees(company_id: int, current_only: bool=False) -> list[Person]:
    """
    Given company id, return list of persons work(ed) for this company
    :param company_id:
    :param current_only: if True, return only people who are currently work in the company
    :return:
    """
    if current_only:
        return list(Employee.objects.filter(company_id=company_id, is_current_job=True))
    return list(Employee.objects.filter(company_id=company_id))


def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    :param person_id:
    :return:
    """
    jobs = Employee.objects.prefetch_related('company_id').filter(person_id=person_id)
    return [{job.company_id.company_name: job.job_title} for job in jobs]

if __name__ == '__main__':
    print(get_person_name_by_id(50))
    print(get_people_cnt_by_gender('Male'))
    print(get_people_by_age(33))
    print(get_companies_by_country('Pakistan'))
    print(get_company_employees(1, True))
    print(get_company_employees(1))
    print(get_person_jobs(68))
