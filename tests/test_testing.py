from gists.testing.test import hello


def test_hello():
    result = hello()
    expected = 'hello'
    assert expected == result
