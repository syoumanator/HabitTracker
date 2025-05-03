import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

load_dotenv()

SU_email = os.getenv("SU_email")
SU_first_name = os.getenv("SU_first_name")
SU_last_name = os.getenv("SU_last_name")
SU_password = os.getenv("SU_password")


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **options):
        User = get_user_model()

        user = User.objects.create(
            email=SU_email,
            first_name=SU_first_name,
            last_name=SU_last_name,
        )
        user.set_password(SU_password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Superuser created: {user.email}"))
