import pytest
import django.db.models as model

@pytest.mark.django_db
def test_my_user():
    me = model.User.objects.get(username='marmo607')
    assert me.is_superuser