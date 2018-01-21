# -*- coding=utf-8 -*-

#这个文件专门执行所有的case
import unittest
#通过主函数调用 如果这个文件不是最初的启动文件，那么main代码块中的语句不能执行
if __name__ == '__main__':
    #我们要找到所有的符合条件的测试用例
    #执行这些测试case
    #defaultTestLoader默认的测试用例加载器
    #discover发现，把发现的测试用例执行
    test_case = unittest.defaultTestLoader.discover('.', pattern='*Test.py')#文件夹、匹配规则文件名、便利到几级目录start_dir, pattern='test*.py', top_level_dir=None
    #文本的测试用例运行器   run执行测试用例并且在控制台输出文本的测试结果

    unittest.TextTestRunner().run(test_case)
    #AAAA