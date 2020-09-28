"""
文件路径
"""
import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)
if __name__ == '__main__':
    a = app_path()
    print(a)