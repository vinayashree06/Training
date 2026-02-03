import pytest
def is_even(n):
    return n%2==0
def test_is_even():
    assert is_even(4)==True
    assert is_even(7)==False
    assert is_even(0)==True
def is_odd(n):
    return n%2!= 0
def test_is_odd():
    assert is_odd(5)==True
    assert is_odd(8)==False
    assert is_odd(0)==False 
if __name__ == '__main__':
    pytest.main()