from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, datetime

# Create your models here.


def get_date_20_years_ago():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return date(year - 20, month, day)


class DefaultUser(AbstractUser):
    USER_TYPES = [
        ('SU', 'superuser'),
        ('CS', 'customer service'),
        ('CU', 'customer'),
    ]
    date_of_brith = models.DateField(default=get_date_20_years_ago())
    image = models.FileField(upload_to="profile_images/", blank=True, null=True)
    type = models.CharField(max_length=2,
                            choices=USER_TYPES,
                            default='CU',
                            )

    def can_delete(self):
        return self.is_superuser_or_staff()

    def has_birthday_today(self):
        return_boolean = False

        now = datetime.now()
        today_month = now.month
        today_day = now.day

        user_month = self.date_of_birth.month
        user_day = self.date_of_birth.day

        if user_month == today_month and user_day == today_day:
            return_boolean = True
        return return_boolean

    def is_superuser_or_customer_service(self):
        if self.type == 'SU' or self.type == 'CS':
            return True
        else:
            return False

    def is_superuser_or_staff(self):
        return self.is_superuser or self.is_staff

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + str(self.date_of_birth) + ')'
    def isStaff(self):
        return self.is_staff

