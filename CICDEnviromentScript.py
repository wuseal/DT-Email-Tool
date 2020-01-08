# 用于该工程的持续集成、部署环境配置的脚本：travis & appveyor
import sys


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


real_tapd_user = sys.argv[1]
real_tapd_password = sys.argv[2]

# 以下为替换为真实的tapd账号信息，替换后打包成可执行文件方可能请求TAPD的api数据
alter("wu/seal/emailtool/TAPD_Constant.py", "{tapd_user}", real_tapd_user)
alter("wu/seal/emailtool/TAPD_Constant.py", "{tapd_password}", real_tapd_password)