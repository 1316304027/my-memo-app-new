#函数outer
def outer(func):
    # 函数内函数inner
    def inner():
        print("===开始===")
        func()
        print('===结束===')
    return inner


# 函数a
def a():
    print("a")

# 函数的执行：返回值传给变量test
test = outer(a)
# 函数的执行
test()

# 函数b
def b(func):
    print("开始")
    func()
    print("结束")

# 函数b的执行
b(a)