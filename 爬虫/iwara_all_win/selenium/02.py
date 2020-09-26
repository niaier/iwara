#
# def 人(name):
#
#     def init(name):
#         人1 = {
#             '姓名': name,
#             '性爱': 做爱,
#             '射精': 射精,
#         }
#         return 人1
#     def 做爱(人):
#         print('%s把鸡巴缓缓插入屄里，再反复抽插出淫水' % 人['姓名'])
#         pass
#     def 射精(人):
#         print('%s浓稠的精液迸射进子宫颈，透传卵巢' % 人['姓名'])
#         pass
#     res =init(name)
#     return res
#     pass
# ren1 = 人('余睿')
# print(ren1)
# ren1['性爱'](ren1)

class people:
    属性 = 123
    def __init__(self,name):
        print('爸爸')
        self.姓名=name
    @property
    def 做爱(self):
        print('%s把鸡巴缓缓插入屄里，再反复抽插出淫水' % self.姓名)
        return '%s把鸡巴缓缓插入屄里，再反复抽插出淫水' % self.姓名
    def 射精(self):
        print('%s浓稠的精液迸射进子宫颈，透传卵巢' % self.姓名)
    # @staticmethod
    # @classmethod

class son(people):
    属性 = 567
    def __init__(self,name):
        self.姓名=name
        self.姓名2=name
    pass

s1 =son('余睿')

print(s1.姓名2)
print(s1.属性)
print(s1.__dict__)
s1.做爱

# p1 = people('余睿')
# p1.做爱
# print(p1.做爱)
# p1.做爱()
# print(people.__dict__)
# print(p1.__dict__)
# print(p1.__dict__['姓名'])
# print(p1.属性)
# print(p1.姓名)
