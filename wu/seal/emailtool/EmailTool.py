import datetime
import logging

from O365 import Account

from wu.seal.emailtool.EmailTemplate import obtainRequestPublishEmailHtmlBody, obtain_table_items, \
    obtain_publish_notify_email_html_body
from wu.seal.emailtool.Utils import Utils

logger = logging.getLogger('Email')
logging.basicConfig(level=logging.INFO)

credentials = ('4a1ce983-de30-4631-ac5c-bfc410e64244', 'jdejIOQMAJ0:;iknK0243):')

account = Account(credentials=('4a1ce983-de30-4631-ac5c-bfc410e64244', 'jdejIOQMAJ0:;iknK0243):'))


# 下面两行代表授权登录过程，有效期只有90天

def printInboxMessage():
    mailbox = account.mailbox()
    inbox = mailbox.inbox_folder()
    for message in inbox.get_messages():
        logger.info(message)
        logger.info(message.sender)


def authontic_work_flow():
    result = account.authenticate(scopes=['basic', 'message_all'])
    info = '成功' if result else '失败'
    print('邮箱账号认证%s' % info)


def sendEmail(subject, to_address_list: list, cc_address_list: list, htmlBody):
    '''发送邮件工具方法'''
    m = account.new_message()
    print("要发送到下列联系人：%s\n并抄送以下联系人：%s" % (to_address_list, cc_address_list))
    m.to.add(to_address_list)
    m.cc.add(cc_address_list)
    m.subject = subject
    m.body = """ <head>
            <style>
            h2 {
                width: 100%%;
                text-align:center;
            }
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%%;
            }

            td, th {
                border: 1px solid #000000;
                text-align: left;
                padding: 8px;
            }

            tr:nth-child(even) {
                background-color: #dddddd;
            }
            </style>
        </head>
                <body>
                    %s
                </body>
                </html>
                """ % htmlBody
    m.send()
    logger.info("邮箱发送成功")


def send_version_commit_request_email(branch_name: str, test=False):
    '''版本提交申请的邮件发送脚本'''
    utils = Utils()
    app_name = utils.getAppName(branch_name)
    app_version = utils.getAppVersion(branch_name)
    apk_link = utils.getAPKLink(branch_name)
    tapd_link = utils.getTapdLink(branch_name)
    logger.info("app name is %s, app version is %s, apk download link is %s, tapd iteration links is %s" % (
        app_name, app_version, apk_link, tapd_link))
    html_body = obtainRequestPublishEmailHtmlBody(app_name=app_name, app_version=app_version, tapd_link=tapd_link,
                                                  apk_link=apk_link)
    subject = "Android-%s-%s 版本提交申请" % (app_name.capitalize(), app_version)
    to_address_list = ['nick.huang@dingtone.me', 'liang.chen@dingtone.me']
    cc_address_list = ['cpl@dingtone.me', 'teresa.gao@dingtone.me', 'neville.chen@dingtone.me',
                       'aaron.zhang@dingtone.me', 'grissom.xue@dingtone.me','kimi.li@dingtone.me']
    to_address_list_test = ['alpha.li@dingtone.me']
    cc_address_list_test = []
    if test:
        sendEmail(subject, to_address_list_test, cc_address_list_test, html_body)
    else:
        sendEmail(subject, to_address_list, cc_address_list, html_body)


def send_publish_notify_email(branch_name: str, open_rate: str = '2%', test=False):
    '''版本发布后的通知邮件'''
    utils = Utils()
    app_name = utils.getAppName(branch_name)
    app_version = utils.getAppVersion(branch_name)
    apk_link = utils.getAPKLink(branch_name)
    tapd_link = utils.getTapdLink(branch_name)
    app_version_code = utils.get_app_version_code(branch_name)
    app_reversion = utils.get_reversion(branch_name)
    table_story_items = obtain_table_items(utils.get_iteration_story_items(branch_name))
    table_bug_items = obtain_table_items(utils.get_iteration_bug_items(branch_name))
    date_time = datetime.datetime.now().__str__()
    date_time = date_time[:date_time.rindex(".")]
    logger.info("app name is %s, app version is %s, apk download link is %s, tapd iteration links is %s" % (
        app_name, app_version, apk_link, tapd_link))
    html_body = obtain_publish_notify_email_html_body(open_rate, app_name, tapd_link, app_version, app_version_code,
                                                      table_story_items, table_bug_items, app_reversion, date_time,
                                                      apk_link)
    subject = "=== Android %s 版本发布专区 ===" % app_name
    to_address_list = ['cpl@dingtone.me', 'QA@dingtone.me']
    cc_address_list = ['steve.wei@dingtone.me', 'peter.wei@dingtone.me',
                       'tiger.liu@dingtone.me', 'liang.chen@dingtone.me', 'kelly.gu@dingtone.me',
                       'teresa.gao@dingtone.me', 'kun.sun@dingtone.me', 'edward.lu@dingtone.me',
                       'nick.huang@dingtone.me', 'locke.meng@dingtone.me',
                       'asher.wang@dingtone.me', 'lisa.huang@dingtone.me', 'bill.yang@dingtone.me',
                       'csqa@dingtone.me', 'kimi.li@dingtone.me','esther.zong@dingtone.me',
                       'coopy.zhou@dingtone.me','abel.li@dingtone.me','locke.meng@dingtone.me']

    to_address_list_test = ['alpha.li@dingtone.me']
    cc_address_list_test = []
    if test:
        sendEmail(subject, to_address_list_test, cc_address_list_test, html_body)
    else:
        sendEmail(subject, to_address_list, cc_address_list, html_body)


if __name__ == '__main__':
    # authontic_work_flow()
    send_publish_notify_email("dingtone_4_15_1", test=True)
    # printInboxMessage()
