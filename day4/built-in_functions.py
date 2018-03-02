# author: zzq

# print(all([1, -5, 3]))
# print(any([]))

# a = ascii([1, 2, "开外挂"])
# print(type(a), [a])

# a = bytes("abcde", encoding="utf-8")
# b = bytearray("abcde", encoding="utf-8")
#
# print(b[1])
# b[1] = 50
# print(b)
# print(a.capitalize(), a)

# def sayhi():pass
#
# print( callable(sayhi))

# (lambda n:print(n))(5)

# res = filter(lambda n:n>5,range(10))

# res = map(lambda n:n*2, range(10))
# res = [lambda i:i*2 for i in range(10)]

# import functools
#
# res = functools.reduce(lambda x, y:x*y, range(1,10))
#
# print(res)

# a = frozenset([1, 4, 333, 212, 33, 33, 12, 4])

# print(globals())

# def test():
#     local_var = 333
#     print(locals())
#     print(globals())
#
# test()
# print(globals())
# print(globals().get('local_val'))

# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# # print(sorted(a.items()))
# print(sorted(a.items(), key=lambda x: x[1]))
#
#
# print(a)

# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
#
#
# for i in zip(a, b):
#     print(i)

__import__('import decorator')
