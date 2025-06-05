from django.core.management.base import BaseCommand
from cvs.management.commands.eng import EngCvSettle


class Command(BaseCommand):
    def handle(self, *args, **options):
        EngCvSettle().settle_cv()
        print("command removed all data from db and populated it with English info")
