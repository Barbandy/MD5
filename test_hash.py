#coding: UTF-8
import hashlib
import pytest
import md5

def hash_md5(data):
    m = hashlib.md5()
    m.update(data)
    return  m.hexdigest()


def test_md5():
    data = ''
    assert hash_md5(data) == md5.calc_md5(data)
	
#if __name__ == '__main__':
   # test_md5()
