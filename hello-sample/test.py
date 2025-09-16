# 模拟一个“Flask”的类
class MiniFlask:
    # __init__() 是类的初始化函数，创建这个类的对象时自动执行。
    def __init__(self):
        #  表示创建一个空字典，来保存路由信息
        self.routes = {}  # 路由表：路径 -> 函数

    def route(self, path):
        def decorator(func):
            # 把字符串"/hello"当作字典的key，把函数hello()本身（不是执行结果）作为value存进去。
            self.routes[path] = func
            # response = self.routes[path]()  # ← 这才是函数的执行！

            return func  # 返回原函数（或你想加工后的）
        return decorator

    def run(self):
        while True:
            path = input("请输入你要访问的网址路径（如 / 或 /hello）：")
            if path in self.routes:
                response = self.routes[path]()  # 执行对应的函数
                print(f"页面内容：{response}")
            else:
                print("404 页面未找到")

# 实例化你的迷你框架
app = MiniFlask()

# 使用自定义的装饰器注册路由
@app.route("/")
def index():
    return "这里是首页"

@app.route("/hello")
def hello():
    return "你好，这是 /hello 页面"

"""
def hello():
    return "你好"

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 这一步是真实注册的灵魂所在

app.routes["/hello"] = hello  # ← 存的是函数 hello（注意没有括号！）


routes = {}

def hello():
    return "你好"

routes["/hello"] = hello  # 注意！不是 hello()

# 模拟访问 /hello 路径：
path = "/hello"
response = routes[path]()  # ← 这里才是真正执行 hello()

print(response)

"""

# 启动“服务器”（其实就是死循环接收输入）
if __name__ == "__main__":
    app.run()
