import factory
from factory.faker import faker
from .models import Record

factory.Faker._DEFAULT_LOCALE = "en_US"


class RecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Record

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email", safe=True, domain="company.org")
    phone = factory.Faker("basic_phone_number")
    address = factory.Faker("street_address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zipcode = factory.Faker("postcode")


# >>> from website.factory import RecordFactory
# >>> x = RecordFactory.create_batch(5)
# >>> exit()
