from django.core.management.base import BaseCommand
from app1.models import Article

from django_seed import Seed
from faker import Faker




class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 Article을 만들겠습니다."

    def add_arguments(self,parser):
        parser.add_argument(
            '--number', default=1, type=int, help="얼마나 생성하시겠습니까?"
        )

    def handle(self,*args,**options):
        number = options.get('number')
        seeder = Seed.seeder()
        fake = Faker(["ko_KR"])
        seeder.add_entity(
            Article,
            number,
            {
                "subject" : lambda x : fake.unique.bs(),
                "content" : lambda x : fake.text()
                # - seeder.faker.address()/name()/text()/sentence()를 사용가능
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}개의 Article을 생성하였습니다."))