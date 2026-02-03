import pytest
def square(n):
    return n*n
def test_square():
    assert square(3)==9
    assert square(-4)==16
    assert square(7)==40
if __name__=='__main__':
    pytest.main()