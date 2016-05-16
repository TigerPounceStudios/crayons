import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import PollChoice
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def poll_choice_factory(db, poll_factory):
    class PollChoiceFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = PollChoice

        poll = factory.SubFactory(poll_factory)
        text = faker.sentence(nb_words=200)

    return PollChoiceFactory


@pytest.fixture
def sample_poll_choice(poll_choice_factory):
    return poll_choice_factory()

