"""
Python 命名空间 LEGB 规则演示
读取: Local → Enclosing → Global → Built-in
赋值: 默认写入 Local，global / nonlocal 跨层写入
"""

# ============================================================
# 1. LEGB 四层查找 (读取规则)
# ============================================================

built_in_demo = "覆盖 len"  # Global 层

def legb_read():
    built_in_demo = "局部变量"  # Local
    print("[读取] Local 覆盖 Global:", built_in_demo)  # 输出局部

legb_read()


# ============================================================
# 2. 赋值默认写入 Local，不影响 Global
# ============================================================

count = 10  # Global

def local_assign():
    count = 999  # 这是 Local 变量，跟 Global 的 count 没关系
    print("[赋值] Local 内的 count:", count)

local_assign()
print("[赋值] Global 的 count 没变:", count, "\n")


# ============================================================
# 3. global — 从内层写入 Global
# ============================================================

score = 60

def modify_global():
    global score       # 声明：我要读写 Global 层的 score
    score = 90
    print("[global] 函数内改为:", score)

modify_global()
print("[global] Global score 变成了:", score, "\n")


# ============================================================
# 4. nonlocal — 写入 Enclosing 层
# ============================================================

def outer():
    msg = "外层"

    def inner():
        nonlocal msg      # 声明：我要读写 outer 里的 msg
        msg = "被 inner 改了"
        print("[nonlocal] inner 内:", msg)

    print("[nonlocal] 调用 outer 前:", msg)
    inner()
    print("[nonlocal] 调用 outer 后:", msg, "\n")

outer()


# ============================================================
# 5. 类有自己的命名空间
# ============================================================

version = "模块级 version"

class Demo:
    version = "类属性 version"    # 在类的命名空间里

    def __init__(self):
        self.version = "实例属性 version"  # 在实例的命名空间里

    def show(self):
        version = "方法局部 version"
        print("[类] 方法局部:", version)
        print("[类] 实例属性:", self.version)
        print("[类] 类属性:", Demo.version)
        print("[类] 模块级:", globals()["version"])

Demo().show()


# ============================================================
# 6. 命名空间本质上是 dict
# ============================================================

print("\n[本质] 当前模块的 Global 命名空间就是字典:")
print("  count  =", globals()["count"])
print("  score  =", globals()["score"])

def foo():
    x = 42
    print("  foo 的 Local 命名空间:", locals())

foo()