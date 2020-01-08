import sys

from wu.seal.emailtool.EmailTool import send_publish_notify_email, send_version_commit_request_email, \
    authontic_work_flow


def __get_test_tip(is_in_test_model):
    if is_in_test_model:
        return "\n------当前为测试模式，所有邮件均会只发送到'seal.wu@dingtone.me'不会发送到其它人------"
    else:
        return "t -> 开启测试模式"


def get_action_prompt(is_in_test_model):
    return f"""
请选择您的操作,输入字符(c/p/a/t):
a -> 进行邮箱授权认证（第一次运行需要进行邮箱授权认证，认证过程可以参考：https://mubu.com/doc/2flgEYrlgE）
c -> 发送版本提交申请邮件
p -> 发送版本发布通知邮件
{__get_test_tip(is_in_test_model)}
"""


branch_name_prompt_for_version_commit_email = """
请输入应用版本申请提交的版本对应的分支名称(例: dev_4_5_0)
dev开头的分支表示期为TalkU
dingtone开头的分支表示其为Dingtone的分支
telos开头的分支表示其为Telos分支
"""

branch_name_prompt_for_veresion_publish_notify_email = """
请输入已经发布的版本对应的分支名称(例: dev_4_5_0)
dev开头的分支表示期为TalkU
dingtone开头的分支表示其为Dingtone的分支
telos开头的分支表示其为Telos分支
(请注意，要严格区分大小写)
"""

roll_out_rate_prompt = """
请输入版本发布后开放的比例:
如果是新包第一次开放则直接输入开放比例，如：2%
如果是扩大开放比例，需要带上上一次的开放比例，如： 2%->5%
"""

sure_to_send_email_prompt = """
确认发送邮件？(y/n)
"""


def go_authenticate_email():
    authontic_work_flow()


def check_roll_out_rate_value(roll_out_rate: str):
    if roll_out_rate.count(r"%") == 2 and roll_out_rate.find('->') == -1:
        print(f"输入的开放比例参数形式不对{roll_out_rate}，退出程序")
        sys.exit(0)


def tipArgs(*args):
    print(f"输入信息为：{args}")


def start(is_in_test_model=False):
    prompt = get_action_prompt(is_in_test_model)
    action_type = input(prompt)
    if action_type == "t":
        start(is_in_test_model=True)
        return
    elif action_type == "a":
        go_authenticate_email()
        return
    elif action_type == "c":
        branch_name = input(branch_name_prompt_for_version_commit_email)
        tipArgs(branch_name)
        sure_to_send_email = input(sure_to_send_email_prompt)
        if sure_to_send_email.lower() == "y":
            send_version_commit_request_email(branch_name, test=is_in_test_model)
        return
    elif action_type == "p":
        branch_name = input(branch_name_prompt_for_veresion_publish_notify_email)
        roll_out_rate = input(roll_out_rate_prompt)
        check_roll_out_rate_value(roll_out_rate)
        tipArgs(branch_name, roll_out_rate)
        sure_to_send_email = input(sure_to_send_email_prompt)
        if sure_to_send_email.lower() == "y":
            send_publish_notify_email(branch_name=branch_name, open_rate=roll_out_rate, test=is_in_test_model)
        return


start()
sys.exit(0)
