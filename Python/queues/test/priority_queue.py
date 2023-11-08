import pytest

from ..objects.plane import Plane
from ..objects.priority_queue import PriorityQueue

def pytest_namespace():
    return {
        'plane1': 0,
        'plane2': 0,
        'plane3': 0,
        'plane4': 0,
        'priority_queue': 0
    }

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
        pytest.plane2 = Plane("FE254", '945', '1230')
        pytest.plane3 = Plane("IQ666", '60', '120')
        pytest.plane4 = Plane("AT864", '415', '500')
        pytest.priority_queue = PriorityQueue()

    def teardown_method(self, method):
        pytest.plane1 = ""
        pytest.plane2 = ""
        pytest.plane3 = ""
        pytest.plane4 = ""
        pytest.priority_queue = ""

    # ======TEST======
    # ----------------
    def test_it_enqueues(self, setup_config):
        pytest.priority_queue.enqueue(0, pytest.plane1)
        pytest.priority_queue.enqueue(2, pytest.plane2)
        pytest.priority_queue.enqueue(2, pytest.plane3)
        pytest.priority_queue.enqueue(4, pytest.plane4)

        assert pytest.priority_queue.total_count() == 4

    def test_it_dequeues(self, setup_config):
        pytest.priority_queue.enqueue(0, pytest.plane1)
        pytest.priority_queue.enqueue(2, pytest.plane2)

        assert pytest.priority_queue.next() == pytest.plane1

    def test_i_peek(self, setup_config):
        pytest.priority_queue.enqueue(0, pytest.plane1)
        pytest.priority_queue.enqueue(2, pytest.plane2)

        assert pytest.priority_queue.peek() == pytest.plane1

    def test_displays_status(self, setup_config):
        pytest.priority_queue.enqueue(0, pytest.plane1)
        pytest.priority_queue.enqueue(2, pytest.plane2)
        pytest.priority_queue.enqueue(2, pytest.plane3)
        pytest.priority_queue.enqueue(4, pytest.plane4)

        assert pytest.priority_queue.status() == '{' + '\n'\
                + '\t0 => 1,\n'\
                + '\t1 => 0,\n'\
                + '\t2 => 2,\n'\
                + '\t3 => 0,\n'\
                + '\t4 => 1,\n'\
                + '\t5 => 0,\n'\
            + '}'

    def test_shows_place_in_queue(self, setup_config):
        pytest.priority_queue.enqueue(0, pytest.plane1)
        pytest.priority_queue.enqueue(4, pytest.plane2)
        pytest.priority_queue.enqueue(3, pytest.plane3)
        pytest.priority_queue.enqueue(2, pytest.plane4)

        assert pytest.priority_queue.queue_wait("UA352") == 0
        assert pytest.priority_queue.queue_wait("FE254") == 3
        assert pytest.priority_queue.queue_wait("IQ666") == 2
        assert pytest.priority_queue.queue_wait("AT864") == 1