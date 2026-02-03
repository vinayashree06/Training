import pytest
def is_palindrome(s):
    return s == s[::-1]
def test_is_palindrome():
    assert is_palindrome("madam")== True
    assert is_palindrome("hello")== False
    assert is_palindrome("racecar")== True
    assert is_palindrome("python")== False
if __name__ == '__main__':
    pytest.main()