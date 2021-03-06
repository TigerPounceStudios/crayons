import pytest
import factory
from faker import Factory as FakerFactory
from django.contrib.auth import get_user_model

from utils.helpers import extend

User = get_user_model()

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def user_factory(db, poll_factory):
    class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = User
                django_get_or_create = ('username', 'email',)

        email = faker.email()
        username = faker.user_name()
        password = factory.PostGenerationMethodCall('set_password', faker.password())

    return UserFactory


@pytest.fixture
def sample_user(user_factory):
    return user_factory()
