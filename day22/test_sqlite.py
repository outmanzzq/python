#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import os, sqlite3


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id varchar(20) PRIMARY KEY , name varchar(20), score int)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    stu_names = []

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM user WHERE score BETWEEN ? AND ? ORDER BY score',(low, high))
    # count = cursor.rowcount
    values = cursor.fetchall()
    cursor.close()
    conn.close()

    if len(values) > 0:
        for name in values:
            stu_names.append(name[0])
        return stu_names


if __name__ == '__main__':
    assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

    print('Pass')
    # print(get_score_in(60, 95))