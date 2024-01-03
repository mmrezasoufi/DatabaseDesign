from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import datetime


class Address(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    building = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    floor = models.IntegerField()
    unit_number = models.IntegerField()
    postal_code = models.CharField(max_length=20)
    coordinate = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)


class Education(models.Model):
    start_date = models.DateField()
    graduation_date = models.DateField()
    major = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    gpa = models.IntegerField()
    institution_name = models.CharField(max_length=255)
    institution_address = models.ForeignKey(Address, on_delete=models.CASCADE)


class PhoneNumber(models.Model):
    PHONE_TYPES = (
        ('Mobile', 'Mobile'),
        ('Work', 'Work'),
        ('Home', 'Home')
    )
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=6, choices=PHONE_TYPES, default='Mobile')


class Person(AbstractUser):
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    persian_first_name = models.CharField(max_length=255)
    persian_last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    national_code = models.CharField(max_length=20, unique=True)
    picture = models.ImageField(upload_to='images/')
    home_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    educations = models.ForeignKey(Education, on_delete=models.CASCADE)
    phone_numbers = models.ManyToManyField(PhoneNumber)

    def clean(self):
        super().clean()
        if not self.phone_numbers.filter(phone_type="Mobile").exists():
            raise ValidationError('One Phone number wit type Mobile is required.')

    def get_age(self):
        """
        Calculate and return user age.
        """
        current_year = datetime.datetime.now().year
        birth_year = self.date_of_birth.year
        return current_year - birth_year

    def get_persian_first_name(self):
        """
        Return the persian_first_name.
        """
        return self.persian_first_name

    def get_persian_last_name(self):
        """
        Return the persian_last_name.
        """
        return self.persian_last_name

    def get_persian_full_name(self):
        """
        Return the persian_first_name and persian_last_name.
        """
        return f'{self.persian_first_name} {self.persian_last_name}'


class Building(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    floors = models.IntegerField()
    capacity = models.IntegerField()
    rooms = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="location")


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    creation_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Office(models.Model):
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)


class Field(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='fields')
    # head_instructor = models.OneToOneField('Instructor', on_delete=models.SET_NULL, null=True, blank=True)


class Employee(Person):
    salary = models.IntegerField()
    hire_date = models.DateField()
    office_hours = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    office = models.ManyToManyField(Office)
    is_committee = models.BooleanField()

    class Meta:
        abstract = True
        proxy = True


class Instructor(Employee):
    instructor_type = models.CharField(max_length=255)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        proxy = True


class Researcher(Employee):
    researcher_type = models.CharField(max_length=255)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        proxy = True

