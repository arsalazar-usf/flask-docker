
# coding=utf-8
import pytest
from pytest_bdd import (
    scenario,
    then,
    when,
)

@pytest.fixture
def my_app():
    from app import app
    return app.test_client().get('/')


@pytest.fixture()
def get_app():
    import app
    return app

@scenario('app.feature', 'Ensure that bye works when given request data')
def test_ensure_that_bye_works_when_given_request_data():
    """Ensure that the bye is working"""

@when("the bye endpoint is hit with correct params")
def the_flask_app_is_imported(get_app):
    assert get_app != None 

@then('the param is returned with bye prepended')
def count_is_incremented_by_a_value_of_one(get_app):
    ret_value = get_app.bye()
    assert ret_value != None