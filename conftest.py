import pytest

from helpers.ri.ri_base_helpers import help_create
from clients.ri_client import ResourceInventoryClient


@pytest.fixture()
def ri():
    return ResourceInventoryClient()


@pytest.fixture()
def create_app(app_ri):
    application_uuid = help_create(app_ri)
    return application_uuid(app_ri)


