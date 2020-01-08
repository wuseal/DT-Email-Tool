# 发布之前的版本申请提交邮件模板,需要处理填充的值有：{app_name},{app_version},{tapd_link},{{apk_link}

__requestPublishhtmlBody = """<p>Aaron&amp;Nick，</p>
<p>Android {app_name}- {app_version} 版本已测试完毕，现准备申请提交审核。请验收该版本质量、需求是否有遗漏，是否允许提交。</p>
<p>TAPD：</p>
<p><a href="{tapd_link}">{tapd_link}</a></p>
<p>{app_name} (PN1 最新包)：</p>
<p><a href="{apk_link}">{apk_link}</a></p>
<p>附上验收清单</p>
<table border = "1" >
<thead>
<tr>
<th><strong>#</strong></th>
<th><strong>版本具体验收清单项</strong></th>
<th><strong>Owner</strong></th>
<th><strong>Result</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>检查PRD任务是否都有完成</td>
<td>产品</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>每一个任务相关的GA事件</td>
<td>产品</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>测试中发现的bug是否还有未解决的（降低优先级,明确不解决的除外）</td>
<td>测试负责人</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>CSQA反馈问题和遗留Bug情况是否处理</td>
<td>测试负责人</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>运营相关的一些检查</td>
<td>运营</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>版本更新日志准备好</td>
<td>运营</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>上线配置和环境准备（配置开关，真实环境验证的case）</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>工具编译再次检测API系统兼容性（Xcode）</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>开发检查版本号（Versioncode+1），最后提交的审核包和Mapping文件</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>需要确认PN1上配置是否有添加（商业化，涉及到配置的功能）</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>是否使用非官方API的检查（针对iOS提交）</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>提交审核相关准备事项（iOS审核开关打开/关闭，通知相关人包括CS人员）</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>审核通过后，开始走Rollout流程</td>
<td>版本Owner</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>Rollout 100%发布后一周，产品决策是否配置升级提示</td>
<td>产品</td>
<td></td>
</tr>
</tbody>
</table>
</br>
Best Regards<br>
<br>
Communication Product Line - Android Team<br>
<br>
<br>
Website: <a href="http://www.tengzhangroup.com/">http://www.tengzhangroup.com</a><br>
<a href="http://www.dingtone.com.cn/">http://www.dingtone.com.cn</a><br>
Twitter:<a href="https://www.twitter.com/dingtone">https://www.twitter.com/dingtone</a><br>
Facebook:<a href="https://www.facebook.com/dingtone">https://www.facebook.com/dingtone</a>
"""

# 版本发布通知邮件模板 需要填充的值有十个：{'{app_revision}', '{open_rate}', '{app_nam}', '{table_items}', '{apk_link}', '{date_time}', '{tapd_link}', '{app_name}', '{app_version_code}', '{app_version}'}
__published_notify_email_template = """<p>Hi, All</p>
<p>Android {app_name} PN1-{app_version}.{app_revision}</p>
<p>新包已经发布，目前开放比例 {open_rate}</p>
<p>App: Android {app_name}</p>
<p>市场：Google Play</p>
<p>版本号：{app_version}</p>
<p>VersionCode：{app_version_code}</p>
<p>开放比例：{open_rate_status}</p>
<p>开放时间：{date_time}</p>
<p>操作：{roll_out_action}</p>
<p>更新：</p>
<table>
<thead>
<tr>
<th>更新功能点：</th>
</tr>
</thead>
<tbody>
{table_story_items}
</tbody>
</table>
<br/>
</br>
<table>
<thead>
<tr>
<th>修复的缺陷点：</th>
</tr>
</thead>
<tbody>
{table_bug_items}
</tbody>
</table>
</br>
</br>
<p><strong>TAPD地址：</strong></p>
<p><a href="{tapd_link}">{tapd_link}</a></p>

<p><strong>PN1地址</strong>：</p>
<p><a href="{apk_link}">{apk_link}</a></p>
<br/>
{roll_out_tip}
</br>
Best Regards<br>
<br>
Communication Product Line - Android Team<br>
<br>
<br>
Website: <a href="http://www.tengzhangroup.com/">http://www.tengzhangroup.com</a><br>
<a href="http://www.dingtone.com.cn/">http://www.dingtone.com.cn</a><br>
Twitter:<a href="https://www.twitter.com/dingtone">https://www.twitter.com/dingtone</a><br>
Facebook:<a href="https://www.facebook.com/dingtone">https://www.facebook.com/dingtone</a>


"""
# 版本发布功能表格的功能点item 模板
__table_item_template = """<tr>
<td><a href="{link}">{item_text}</a></td>
</tr>"""

__roll_out_first_step_notify_html_template_with_app_see_content = """<p><strong>当前开启到{open_rate}，预计12小时后开启5%:</strong></p>
<p>Rollout条件：</p>
<p>1，Crash和ANR异常。 --- 负责人：版本Owner</p>
<p>2，GA产品业务数据是否有重大异常。产品跟进各个开发Owner，需要产品落实到每一个开发。--- 负责人：产品：<a href="mailto:nick.huang@dingtone.me">@Nick</a>。</p>
<br/>
<p>请相关人员回复该邮件，不回复则不会进行下一步rollout流程</p>
<h1 class="atx" id="-">，请知悉！</h1>

"""

__roll_out_second_step_notify_html_template_with_app_see_content = """<p><strong>当前已经开启{open_rate}，下一步预计什么时候开启20%或者50%:</strong></p>
<p>Rollout条件：</p>
<p>1，Crash和ANR --- 负责人：版本Owner</p>
<p>2，业务优化数据等等。--- 负责人：产品：<a href="mailto:nick.huang@dingtone.me">@Nick</a>。</p>
<br/>
<p>请相关人员回复该邮件，不回复则不会进行下一步rollout流程</p>
<h1 class="atx" id="-">，请知悉！</h1>
"""

__roll_out_third_step_notify_html_template = """<p><strong>当前已经开启{open_rate}，下一步预计什么时候开启100%:</strong></p>
<p>Rollout条件：</p>
<p>1，Crash和ANR --- 负责人：版本Owner</p>
<p>2，业务优化数据等等。--- 负责人：产品：<a href="mailto:nick.huang@dingtone.me">@Nick</a>。</p>
<br/>
<p>请相关人员回复该邮件，不回复则不会进行下一步rollout流程</p>
<h1 class="atx" id="-">，请知悉！</h1>
"""

__roll_out_first_step_notify_html_template_without_app_see_content = """<p><strong>当前开启到{open_rate}，预计12小时后开启5%:</strong></p>
<p>Rollout条件：</p>
<p>1，Crash和ANR异常。 --- 负责人：版本Owner</p>
<p>2，GA产品业务数据是否有重大异常。产品跟进各个开发Owner，需要产品落实到每一个开发。--- 负责人：产品：<a href="mailto:nick.huang@dingtone.me">@Nick</a>。</p>
<br/>
<p>请相关人员回复该邮件，不回复则不会进行下一步rollout流程</p>
<h1 class="atx" id="-">，请知悉！</h1>

"""

__roll_out_second_step_notify_html_template_without_app_see_content = """<p><strong>当前已经开启{open_rate}，下一步预计什么时候开启20%或者50%:</strong></p>
<p>Rollout条件：</p>
<p>1，Crash和ANR --- 负责人：版本Owner</p>
<p>2，业务优化数据等等。--- 负责人：产品：<a href="mailto:nick.huang@dingtone.me">@Nick</a>。</p>
<br/>
<p>请相关人员回复该邮件，不回复则不会进行下一步rollout流程</p>
<h1 class="atx" id="-">，请知悉！</h1>
"""


class Item:
    def __init__(self, item_name, item_url):
        self.item_name = item_name
        self.item_url = item_url

    def __str__(self):
        return f"name is {self.item_name}, url is {self.item_url}"


def obtain_table_items(items: list):
    '''根据入参转换获取相应的表格html格式内容'''
    table_items_html = ""
    for item in items:
        table_items_html += __table_item_template.replace('{item_text}', item.item_name).replace('{link}',
                                                                                                 item.item_url)
    return table_items_html


def obtainRequestPublishEmailHtmlBody(app_name, app_version, tapd_link, apk_link):
    '''获取版本申请发布的邮件html body,用于后面流程中嵌入html整体中'''
    return __requestPublishhtmlBody.replace("{app_name}", app_name).replace("{app_version}", app_version).replace(
        "{tapd_link}", tapd_link).replace("{apk_link}", apk_link)


def obtain_publish_notify_email_html_body(open_rate_status: str,
                                          app_name:str,
                                          tapd_link,
                                          app_version,
                                          app_version_code,
                                          table_story_items,
                                          table_bug_items,
                                          app_revision,
                                          date_time,
                                          apk_link):
    open_rate = open_rate_status.split('->')[-1]

    open_rate_float = float(open_rate.replace("%", ""))
    # 只有talku才会有app see的配置描述提示
    if app_name.lower().__contains__("talku"):
        if 5 > open_rate_float >= 1:
            roll_out_tip = __roll_out_first_step_notify_html_template_with_app_see_content.replace('{open_rate}', open_rate)
        elif 20 > open_rate_float >= 5:
            roll_out_tip = __roll_out_second_step_notify_html_template_with_app_see_content.replace('{open_rate}', open_rate)
        elif 50 > open_rate_float >= 20:
            roll_out_tip = __roll_out_third_step_notify_html_template.replace('{open_rate}', open_rate)
        else:
            roll_out_tip = ""
    else:
        if 5 > open_rate_float >= 1:
            roll_out_tip = __roll_out_first_step_notify_html_template_without_app_see_content.replace('{open_rate}', open_rate)
        elif 20 > open_rate_float >= 5:
            roll_out_tip = __roll_out_second_step_notify_html_template_without_app_see_content.replace('{open_rate}', open_rate)
        elif 50 > open_rate_float >= 20:
            roll_out_tip = __roll_out_third_step_notify_html_template.replace('{open_rate}', open_rate)
        else:
            roll_out_tip = ""

    return __published_notify_email_template.replace("{open_rate_status}", open_rate_status).replace("{app_name}",
                                                                                                     app_name).replace(
        '{tapd_link}', tapd_link).replace('{app_version}', app_version).replace("{app_version_code}",
                                                                                app_version_code).replace(
        '{table_story_items}', table_story_items).replace('{table_bug_items}', table_bug_items).replace(
        '{app_revision}',
        app_revision).replace(
        '{date_time}', date_time).replace('{apk_link}', apk_link).replace("{open_rate}",
                                                                          open_rate).replace(
        '{roll_out_action}', "新包" if open_rate_status.split('->').__len__() == 1 else "扩大开放比例").replace(
        "{roll_out_tip}", roll_out_tip)
