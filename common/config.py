"""
用来读取配置文件
"""

import json
import os
from tkinter import messagebox

# 清除 pygame 狗屎输出
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

# 防止变量被其他模块导入造成污染
__all__ = ["get_config", "get_config_all", "write_config", "save_config", "reload_config", 'abs_path']


# 绝对路径，防止外部运行某个脚本无法定位目录
def abs_path(path: str):
    return os.path.normpath(os.path.join(os_path, path))


os_path = os.path.dirname(os.path.abspath(__file__))
config_path = abs_path("../config.json")


def error_message(message):
    # 创建一个简单的Tkinter警告弹窗
    messagebox.showerror("别乱改配置文件", message)

def get_config(key: str) -> any:
    """
    读取配置文件的至
    :param key: 配置的键
    :return:
    """
    return data[key]

def get_config_all() -> dict:
    """
    获取配置的字典对象本身
    :return: 一个字典
    """
    return data

def write_config(key: str, value: any) -> bool:
    """
    写入/修改配置
    :param key: 配置的键
    :param value: 配置的值
    :return:
    """
    data[key] = value
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            # noinspection PyTypeChecker
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        messagebox.showerror("丸辣", "写入配置文件失败\n" + str(e))
        return False



def save_config() -> bool:
    """
    保存配置，和 write_config 二选一
    :return:返回是否保存成功
    """
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            # noinspection PyTypeChecker
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        messagebox.showerror("丸辣", "写入配置文件失败\n" + str(e))
        return False

def reload_config():
    global data
    try:
        with open(config_path, 'r', encoding='utf-8',) as f:
            data = json.load(f)

    except FileNotFoundError:
        error_message("未找到配置文件")
    except json.JSONDecodeError:
        error_message("配置文件不是有效的 JSON 格式")

try:
    with open(config_path, 'r', encoding='utf-8',) as file:
        data = json.load(file)

except FileNotFoundError:
    error_message("未找到配置文件")
except json.JSONDecodeError:
    error_message("配置文件不是有效的 JSON 格式")


