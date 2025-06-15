from utils.helper import Helper

def test_commit_types():
    assert "feat" in Helper.commit_message_types
    assert "fix" in Helper.commit_message_types


def test_commit_message_example():
    assert "feat: add hat wobble" in Helper.commit_message_example 