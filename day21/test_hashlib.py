#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import hashlib


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    if isinstance(password, str):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()
    else:
        raise ValueError('invalid input error!')


def login(user, password):
    for u, p in db.items():
        if user == u and calc_md5(password) == p:
            return True
            break
    return False


if __name__ == '__main__':
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')