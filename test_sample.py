import pytest
def func(x):
    return x+5
def test_method():
    assert func(3)==8
    assert func(-2)==5

if __name__=='__main__':
    pytest.main()
