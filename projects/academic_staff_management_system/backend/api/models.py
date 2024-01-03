from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import datetime


class Address(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    building_name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    floor = models.IntegerField()
    unit_number = models.IntegerField()
    plate_number = models.CharField(max_length=10)
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
    PHONE_TYPES = (("Mobile", "Mobile"), ("Work", "Work"), ("Home", "Home"))
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=6, choices=PHONE_TYPES, default="Mobile")


class Person(AbstractUser):
    GENDER_TYPES = (("M", "Male"), ("F", "Female"))
    persian_first_name = models.CharField(max_length=255)
    persian_last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    national_code = models.CharField(max_length=20, unique=True)
    picture = models.ImageField(upload_to="images/")
    home_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    educations = models.ForeignKey(Education, on_delete=models.CASCADE)
    phone_numbers = models.ManyToManyField(PhoneNumber)

    def clean(self):
        super().clean()
        if not self.phone_numbers.filter(phone_type="Mobile").exists():
            raise ValidationError("One Phone number wit type Mobile is required.")

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
        return f"{self.persian_first_name} {self.persian_last_name}"


class Building(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    floors = models.IntegerField()
    capacity = models.IntegerField()
    rooms = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


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
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)


class Employee(Person):
    salary = models.IntegerField()
    hire_date = models.DateField()
    office_hours = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    office = models.ManyToManyField(Office)
    is_committee = models.BooleanField()


class Field(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="fields"
    )
    head = models.OneToOneField(
        "Instructor", on_delete=models.SET_NULL, null=True, related_name="head_of_field"
    )


class Instructor(Employee):
    instructor_type = models.CharField(max_length=255)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    is_in_committee = models.BooleanField(default=False)


class Researcher(Employee):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)


class Research(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    search_area = models.TextField()
    funding_source = models.TextField()
    budget = models.IntegerField()
    discription = models.TextField()
    publication = models.TextField()
    keywords = models.TextField()
    STATUS_CHOICE = [("ToDo", "ToDo"), ("InProgress", "InProgress"), ("Done", "Done")]
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="ToDo")
    website = models.TextField()
    related_research = models.TextField()


class ResearchMember(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, null=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)


class Schedule(models.Model):
    DAY_CHOICES = [
        ("Sat", "Satureday"),
        ("Sun", "Sunday"),
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
    ]
    day = models.CharField(choices=DAY_CHOICES, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Labratory(models.Model):
    name = models.CharField(max_length=255)
    equipments = models.TextField()
    capacity = models.IntegerField()
    budget = models.IntegerField()
    managers = models.ManyToManyField(Employee)
    schedules = models.ManyToManyField(Schedule)


class Library(models.Model):
    name = models.CharField(max_length=255)
    capcity = models.IntegerField()
    books = models.IntegerField()
    managers = models.ManyToManyField(Employee)
    schedules = models.ManyToManyField(Schedule)
