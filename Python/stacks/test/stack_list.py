import pytest

from ..objects.stack_list import Stack

def pytest_namespace():
    return {'stack': 0}

@pytest.fixture
def setup_config():
    # Setup configuration
    yield
    # Teardown configuration

class TestExample:
    # ===SETUP===
    # -----------
    def setup_method(self, method):
        pytest.stack = Stack()

    def teardown_method(self, method):
        pytest.stack = ""

    # ===TEST===
    # -----------
    def test_i_peeks(self, setup_config):
        pytest.stack.push("A")
        pytest.stack.push("B")
        pytest.stack.push("C")

        assert pytest.stack.peek() == "C"

    def test_check_empty(self, setup_config):
        pytest.stack.push("A")
        pytest.stack.push("B")
        pytest.stack.push("C")

        assert pytest.stack.pop() == "C"
        assert pytest.stack.pop() == "B"
        assert pytest.stack.pop() == "A"

        assert pytest.stack.empty() == True

    def test_it_pushes(self, setup_config):
        pytest.stack.push("A")
        pytest.stack.push("B")
        pytest.stack.push("C")

        assert pytest.stack.count() == 3

    def test_it_pops(self, setup_config):
        pytest.stack.push("A")
        pytest.stack.push("B")
        pytest.stack.push("C")

        assert pytest.stack.pop() == "C"
        assert pytest.stack.pop() == "B"
        assert pytest.stack.pop() == "A"

    def test_reverse_string(self, setup_config):
        string = "abcdef"

        for char in string:
            pytest.stack.push(char)
        pytest.stack.reverse_stack()

        assert pytest.stack.print_stack() == "fedcba"
