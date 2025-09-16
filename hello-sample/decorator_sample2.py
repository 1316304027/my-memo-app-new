#函数outer
def outer(func):
    # 函数内函数inner
    def inner(*args,**kwargs):
        print("===开始===")
        func(*args,**kwargs)
        print('===结束===')
    return inner

#
nums=(10,20,30,40)
#函数show_sum
@outer
def show_sum(nums):
    sum=0
    for num in nums:
        sum+=num
    print(sum)
#@outer是一个函数装饰器，它能在不修改原函数代码的情况下，给函数添加额外的功能（这里是在函数调用前后打印分隔线）。

#字典
users={'张三': 30 , '赵四':40,'王五':50}
@outer
def show_info(users):
    for name,age in users.items():
        print(f'名前:{name},年龄:{age}')

#函数执行
show_sum(nums)
show_info(users)
