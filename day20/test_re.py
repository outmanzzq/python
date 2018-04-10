#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import re


def is_valid_email(addr):
    if re.match(r'^[a-z][0-9a-zA-Z\_\.]+@\w+\.\w{2,3}$', addr):
        return True


def name_of_email(addr):
    re_email = re.match(r'^<', addr)

    if re_email:
        return re.match(r'<([a-zA-Z]+\s+?\w+)>\s+([0-9a-zA-Z]+)@', addr).group(1)
    else:
        return re.match(r'([0-9a-z-A-Z_]+)@', addr).group(1)


# 测试
if __name__ == '__main__':
    # 作业一
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print('ok')

    # 作业二
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    print('ok')