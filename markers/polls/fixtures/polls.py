import pytest
import factory
from faker import Factory as FakerFactory

from polls.models import Poll
from utils.helpers import extend

faker = FakerFactory.create()
faker.seed(1234)


@pytest.fixture
def poll_factory(db, topic_factory):
    class PollFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Poll
                django_get_or_create = ('name',)

        name = faker.sentence(nb_words=10)
        info = faker.sentence(nb_words=200)
        topic = factory.SubFactory(topic_factory)

    return PollFactory


@pytest.fixture
def sample_poll(poll_factory):
    return poll_factory()


@pytest.fixture
def sample_full_poll_data_no_responses(topic_factory, poll_factory, poll_choice_factory):
    topic = topic_factory(name="Wildlife")
    poll = poll_factory(name="New State Bird", topic=topic)
    first_poll_choice = poll_choice_factory(text="Pidgey", poll=poll)
    second_poll_choice = poll_choice_factory(text="A Porcupine", poll=poll)
    return poll

@pytest.fixture
def sample_full_poll_data_with_responses(user_factory, sample_full_poll_data_no_responses, response_factory):
    bob = user_factory(username="bob")
    tom = user_factory(username="tom")
    poll = sample_full_poll_data_no_responses
    poll_choices = poll.pollchoice_set.all()

    response_factory(poll_choice=poll_choices[0], user=bob)
    response_factory(poll_choice=poll_choices[1], user=tom)
    return poll
