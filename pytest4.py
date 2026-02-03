import pytest
def total(lst):
    return sum(lst)
def maximum(lst):
    return max(lst)
def test_total():
    assert total([1,2,3])==6
def test_max():
    assert maximum([1,5,3])==5
if __name__=='__main__':
    pytest.main()