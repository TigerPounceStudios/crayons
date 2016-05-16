import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Topic
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def topic_factory(db):
    class TopicFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Topic

        name = faker.sentence(nb_words=5)

    return TopicFactory


@pytest.fixture
def sample_topic(topic_factory):
    return topic_factory()
