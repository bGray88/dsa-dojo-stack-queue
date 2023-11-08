import pytest

from ..objects.queue_normal import Queue

def pytest_namespace():
    return {'queue': 0}

@pytest.fixture
def setup_config():
    # Setup configuration
    yield
    # Teardown configuration

class TestExample:
    # =====SETUP=====
    # ---------------
    def setup_method(self, method):
        pytest.queue = Queue()

    def teardown_method(self, method):
        pytest.queue = ""

    # ======TEST======
    # ----------------
    def test_it_enqueues(self, setup_config):
        pytest.queue.enqueue("A")
        pytest.queue.enqueue("B")
        pytest.queue.enqueue("C")

        assert pytest.queue.count() == 3

    def test_it_dequeues(self, setup_config):
        pytest.queue.enqueue("A")
        pytest.queue.enqueue("B")
        pytest.queue.enqueue("C")

        assert pytest.queue.dequeue() == "A"
        assert pytest.queue.dequeue() == "B"
        assert pytest.queue.dequeue() == "C"
    
    def test_i_peeks(self, setup_config):
        pytest.queue.enqueue("A")
        pytest.queue.enqueue("B")
        pytest.queue.enqueue("C")

        assert pytest.queue.peek() == "A"

    def test_i_last(self, setup_config):
        pytest.queue.enqueue("A")
        pytest.queue.enqueue("B")
        pytest.queue.enqueue("C")

        assert pytest.queue.last() == "C"

    def test_check_empty(self, setup_config):
        pytest.queue.enqueue("A")
        pytest.queue.enqueue("B")
        pytest.queue.enqueue("C")

        assert pytest.queue.dequeue() == "A"
        assert pytest.queue.dequeue() == "B"
        assert pytest.queue.dequeue() == "C"

        assert pytest.queue.empty() == True
