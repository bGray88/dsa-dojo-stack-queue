import pytest

from ..objects.plane import Plane

def pytest_namespace():
    return {'plane1': 0}

@pytest.fixture
def setup_config():
    # Setup configuration
    yield
    # Teardown configuration

class TestExample:
    # =====SETUP=====
    # ---------------
    def setup_method(self, method):
        pytest.plane1 = Plane("UA352", '510', '615')


    def teardown_method(self, method):
        pytest.plane1 = ""

    # ======TEST======
    # ----------------
    def test_it_creates(self, setup_config):
        assert pytest.plane1.name == "UA352"
        assert pytest.plane1.expected_departure == "510"
        assert pytest.plane1.expected_landing == "615"
