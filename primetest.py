import pytest
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
def test_is_prime():
    assert is_prime(2)==True
    assert is_prime(3)==True
    assert is_prime(4)==False
if __name__=="__main__":
    pytest.main()