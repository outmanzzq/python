# author: zzq


class AlexException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'sdsf'


try:
    # name = []
    # name[3]
    raise AlexException('数据库连不上！')
except AlexException as e:
    print(e)