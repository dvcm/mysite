import pytest

from blog.factories import PostFactory
from blog.src.models import Post


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest whit factory'
