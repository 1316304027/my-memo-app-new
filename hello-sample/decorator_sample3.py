#函数outer
def outer(func):
    # 函数内函数inner
    def inner():
        print("===开始===")
        func()
        print('===结束===')
    return inner


# 函数a
@outer
def a():
    print("a")

# 函数的执行：返回值传给变量test
test = outer(a)
# 函数的执行
test()

# 函数b
@outer
def b():
    print("b")

# 函数的执行
b()
a()

"""
test() → new_inner()
    → print("开始")         # 第二层壳
    → inner()              # 第一次装饰的inner
        → print("开始")     # 第一层壳
        → a()              # 原函数（此时a已被替换，此处是历史命名遗留问题）
            → print("a")   # 核心逻辑
        → print("结束")     # 第一层壳
    → print("结束")         # 第二层壳

"""

