from domain.errors import GitError

def test_git_error_str():
    err = GitError("Some error message")
    assert str(err) == "❌ Some error message"


def test_git_error_internet():
    err = GitError.internet_connection()
    assert "No internet connection" in str(err) 