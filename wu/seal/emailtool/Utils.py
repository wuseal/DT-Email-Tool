import base64
import logging

import requests
import json
import sys

# 加上下面这一行后就可以单独在根目录运行这个文件了
sys.path.append('')
from bs4 import BeautifulSoup
from wu.seal.emailtool.EmailTemplate import Item
from wu.seal.emailtool.TAPD_Constant import tapd_api_user, tapd_api_password


class Utils:
    __logger = logging.getLogger('Utils')
    __apk_link_template = """http://10.88.0.132/{app_name_lower_case}_{branch_name}/pn1/{app_version}/index.html"""
    __iteration_item_story_link_template = """https://www.tapd.cn/33700533/prong/stories/view/{story_id}"""
    __iteration_item_bug_link_template = """https://www.tapd.cn/33700533/bugtrace/bugs/view?bug_id={story_id}"""

    def getAppName(self, branch_name: str):
        if "dingtone" in branch_name.lower():
            return "Dingtone"
        elif "telos" in branch_name.lower():
            return "Telos"
        elif "number" in branch_name.lower():
            return "2nd Number"
        else:
            return "TalkU"

    def getAppVersion(self, branch_name: str):
        temp = branch_name[branch_name.index("_") + 1:]
        main_version = temp[0:temp.index("_")]
        temp = temp[temp.index("_") + 1:]
        minor_version = temp[0:temp.index("_")]
        temp = temp[temp.index("_") + 1:]
        if temp.__contains__("_"):
            micro_version = temp[0:temp.index("_")]
        else:
            micro_version = int(temp)

        return f"{main_version}.{minor_version}.{micro_version}"

    def getAPKLink(self, branch_name: str):
        app_name = self.getAppName(branch_name).lower()
        if app_name.__contains__("number"):
            # 2nd Number在Jenkins打好包的下载链接对应的应用名字是number，所以这里替换下
            app_name = "number"
        return self.__apk_link_template.replace("{app_name_lower_case}", app_name).replace(
            "{branch_name}", branch_name.lower()).replace("{app_version}", self.getAppVersion(branch_name))

    def __get_current_iteration_id(selfs, branch_name: str):
        '''获取当前的git分支对应的版本迭代ID'''
        app_name = selfs.getAppName(branch_name)
        app_version = selfs.getAppVersion(branch_name)
        __iterations_url: str = "https://api.tapd.cn/iterations"
        get_response = requests.get(url=__iterations_url,
                                    params={"workspace_id": "33700533", "page": 1, "limit": 100, "status": "open"},
                                    auth=(tapd_api_user, tapd_api_password))
        __json = json.loads(get_response.text)
        selfs.__logger.info("抓取到的版本迭代列表为：%s" % __json)
        iteration_id: str = None
        for each in __json['data']:
            iteration_name: str = each['Iteration']['name']
            if "android" in iteration_name.lower() and app_version.lower() in iteration_name.lower() and app_name.lower() in iteration_name.lower():
                iteration_id = each['Iteration']["id"]
                break

        if iteration_id is None:
            selfs.__logger.error("没有获取到TAPD上的版本迭代信息，请确认TAPD上有建相应的版本迭代")
        return iteration_id

    def getTapdLink(selfs, branch_name: str):
        iteration_id = selfs.__get_current_iteration_id(branch_name)
        __tapd_iteration_link_template = "https://www.tapd.cn/33700533/prong/iterations/view/{iteration_id}"
        tapd_iteration_link = __tapd_iteration_link_template.replace('{iteration_id}', iteration_id)
        return tapd_iteration_link

    def get_reversion(self, branch_name: str):
        apk_link = self.getAPKLink(branch_name)
        self.__logger.info("组装后的APK下载页链接地址为：%s" % apk_link)
        req = requests.get(apk_link)
        bfs = BeautifulSoup(req.text, "html.parser")
        detail_version_info: str = bfs.find('td', class_="instructions_app").string
        return detail_version_info[detail_version_info.rindex(".") + 1:]

    def get_app_version_code(self, branch_name: str):
        app_name = self.getAppName(branch_name)
        git_lab_access_token = """U4E2RNTg5Aobk3NUUs-K"""
        if app_name.lower() == "telos":
            get_file_url = """http://10.88.0.31/api/v3/projects/121/repository/files?private_token=%s&file_path=build.gradle&ref=%s""" % (
                git_lab_access_token, branch_name)
            responseContentText = requests.get(get_file_url).text
            loadedJSON = json.loads(responseContentText)
            self.__logger.info(f"从gitlab 读取到的内容是{responseContentText},加载后的JSON 是{loadedJSON}")
            __content: str = str(base64.b64decode(loadedJSON['content']))
            self.__logger.info(f"最后取得的build.gradle文件的内容是{__content}")
            left = __content.index("{")
            right = __content.index("}")
            app_info = __content[left + 1:right].replace(r"\n", "\n").strip()
            app_version_code_line = app_info.split("\n")[1]
            app_version_code = app_version_code_line.split("=")[1].strip()
            return app_version_code
        elif app_name.lower() == "2nd number":
            get_file_url = """http://10.88.0.31/api/v3/projects/107/repository/files?private_token=%s&file_path=DingtoneAndroid/config.gradle&ref=%s""" % (
                git_lab_access_token, branch_name)
            __content: str = str(base64.b64decode(json.loads(requests.get(get_file_url).text)['content']))
            left = __content.index("number")
            right = __content.rindex(r"}")
            content = __content[left:right].replace(r"\n", "")
            configs = content.split("] ")
            # 配置文件里的app name是number所以这里要使用number这个字符查找version code的值
            config_app_name = "number"
            for each in configs:
                if config_app_name in each.lower():
                    return each[each.index(":") + 1:each.index(",")].strip()
        else:
            get_file_url = """http://10.88.0.31/api/v3/projects/4/repository/files?private_token=%s&file_path=DingtoneAndroid/config.gradle&ref=%s""" % (
                git_lab_access_token, branch_name)
            __content: str = str(base64.b64decode(json.loads(requests.get(get_file_url).text)['content']))
            left = __content.index("talku")
            right = __content.rindex(r"}")
            content = __content[left:right].replace(r"\n", "")
            configs = content.split("] ")
            for each in configs:
                if app_name.lower() in each.lower():
                    return each[each.index(":") + 1:each.index(",")].strip()

    def get_iteration_story_items(self, branch_name: str):
        iteration_id = self.__get_current_iteration_id(branch_name)
        self.__logger.info("抓取到的版本迭代id为：%s" % iteration_id)
        items = list()
        self.__get_iteration_story_item_list(items, iteration_id)
        return items

    def get_iteration_bug_items(self, branch_name: str):
        iteration_id = self.__get_current_iteration_id(branch_name)
        self.__logger.info("抓取到的版本迭代id为：%s" % iteration_id)
        items = list()
        self.__get_iteration_bug_item_list(items, iteration_id)

        return items

    def __get_iteration_story_item_list(self, items, iteration_id):
        __stories_url: str = "https://api.tapd.cn/stories"
        get_response = requests.get(url=__stories_url,
                                    params={"workspace_id": "33700533", "iteration_id": iteration_id, "page": 1,
                                            "limit": 100},
                                    auth=(tapd_api_user, tapd_api_password))
        __json = json.loads(get_response.text)
        self.__logger.info("抓取到的版本迭代对应的需求列表为：%s" % __json)
        for item in __json['data']:
            item_name = item["Story"]['name']
            item_link = self.__iteration_item_story_link_template.replace('{story_id}', item["Story"]['id'])
            items.append(Item(item_name, item_link))

    def __get_iteration_bug_item_list(self, items, iteration_id):
        __bugs_url: str = "https://api.tapd.cn/bugs"
        get_response = requests.get(url=__bugs_url,
                                    params={"workspace_id": "33700533", "iteration_id": iteration_id, "page": 1,
                                            "limit": 100},
                                    auth=(tapd_api_user, tapd_api_password))
        __json = json.loads(get_response.text)
        self.__logger.info("抓取到的版本迭代对应的缺陷列表为：%s" % __json)
        for item in __json['data']:
            item_name = item["Bug"]['title']
            item_link = self.__iteration_item_bug_link_template.replace('{story_id}', item["Bug"]['id'])
            items.append(Item(item_name, item_link))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    result = Utils().get_app_version_code("telos_2_1_7")
    print(result)
