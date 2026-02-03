import pytest
def test_answer1():
    a=5
    b=10
    assert a==b
def test_answer2():
    c=15
    d=3*5
    assert c==d
def test_answer3():
    x=7
    y=14
    assert x*2==y
def test_answer4():
    p=20
    q=4*5
    assert p==q
def test_answer5():
    m=9
    n=3*3
    assert m==n
if __name__=='__main__':
    pytest.main()