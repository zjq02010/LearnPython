
class TEST_module():
    def __init__(self):
        self.auth = None
        self.proxy = {}


    def pri1(self, user):
        print("这是另一个测试模块里面的测试输出函数pri1",user)

    def pri2(self, password):
        print("这是另一个测试模块里面的测试输出函数pri2", password)

    def pri3(self,proxy):
        print("这是另一个测试模块里面的测试输出函数pri2", proxy)
