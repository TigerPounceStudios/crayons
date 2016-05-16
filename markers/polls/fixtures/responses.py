import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import PollResponse
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def response_factory(db, user_factory, poll_choice_factory):
    class ResponseFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = PollResponse

        user = factory.SubFactory(user_factory)
        poll_choice = factory.SubFactory(poll_choice_factory)

    return ResponseFactory


@pytest.fixture
def sample_response(response_factory):
    return response_factory()

