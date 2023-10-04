import os
from enum import IntEnum
from typing import List

from flask import Flask, request
from plugins.autoRepoke import AutoRepoke
from plugins.faq_v2 import MaintainFAQ, AskFAQ, HelpFAQ
from plugins.showMCStatus_v3 import (
    ShowMcStatus,
    McStatusAddServer,
    McStatusRemoveServer,
    McStatusSetFooter,
    McStatusRemoveFooter,
)
from plugins.superEmoji import (
    FirecrackersFace,
    FireworksFace,
    BasketballFace,
    HotFace,
    FlowerFace,
    VegDog,
    TouchFace,
    BirthdayCake,
    ff98sha,
)
from utils.accountOperation import create_account_sql
from utils.basicConfigs import APPLY_GROUP_ID, APPLY_GUILD_ID
from utils.basicEvent import warning, set_friend_add_request, set_group_add_request
from utils.configAPI import createGlobalConfig
from utils.configsLoader import createApplyGroupsSql, loadApplyGroupId
from utils.sqlUtils import createBotDataDb
from utils.standardPlugin import NotPublishedException
from utils.standardPlugin import (
    StandardPlugin,
    PluginGroupManager,
    EmptyPlugin,
    PokeStandardPlugin,
    AddGroupStandardPlugin,
    GuildStandardPlugin,
)

try:
    from plugins.mua import (
        MuaAnnHelper,
        MuaAnnEditor,
        MuaTokenBinder,
        MuaTokenUnbinder,
        MuaTokenEmpower,
        MuaTokenLister,
        MuaNotice,
        MuaQuery,
        MuaAbstract,
        MuaGroupBindTarget,
        MuaGroupUnbindTarget,
        MuaGroupAnnFilter,
    )
except NotPublishedException as e:
    print("mua plugins not imported: {}".format(e))
    MuaAnnHelper, MuaAnnEditor = EmptyPlugin, EmptyPlugin
    MuaTokenBinder, MuaTokenUnbinder, MuaTokenEmpower = (
        EmptyPlugin,
        EmptyPlugin,
        EmptyPlugin,
    )
    uaTokenLister, MuaNotice, MuaQuery, MuaAbstract = (
        EmptyPlugin,
        EmptyPlugin,
        EmptyPlugin,
        EmptyPlugin,
    )
    MuaGroupBindTarget, MuaGroupUnbindTarget = EmptyPlugin, EmptyPlugin
    MuaGroupAnnFilter = EmptyPlugin
    MuaTokenLister = EmptyPlugin
from plugins.help_v2 import ShowHelp, ShowStatus, ServerMonitor
from plugins.groupBan import UserBan, BanImplement, GetBanList
from plugins.privateControl import PrivateControl, LsGroup, GroupApply, HelpInGroup
from plugins.bilibiliSubscribe_v2 import BilibiliSubscribe, BilibiliSubscribeHelper
from plugins.getPermission import (
    AddPermission,
    DelPermission,
    ShowPermission,
    AddGroupAdminToBotAdmin,
)
from plugins.messageRecorder import GroupMessageRecorder
from plugins.addGroupRecorder import AddGroupRecorder
from plugins.gocqWatchDog import GocqWatchDog


def sqlInit():
    createBotDataDb()
    createApplyGroupsSql()
    createGlobalConfig()
    create_account_sql()

    loadApplyGroupId()
    # removeInvalidGroupConfigs() # it may danger, consider change it to add tag


sqlInit()  # put this after import

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")

# 特殊插件需要复用的放在这里
helper = ShowHelp()  # 帮助插件
helperForPrivateControl = HelpInGroup()  # BOT管理员查看群聊功能开启情况插件
gocqWatchDog = GocqWatchDog(60)
groupMessageRecorder = GroupMessageRecorder()  # 群聊消息记录插件
banImpl = BanImplement()
# BilibiliLiveMonitor(30539032, 'MUA', 'mualive')
# GetBilibiliLive(30539032, 'MUA', '-mualive')

GroupPluginList: List[StandardPlugin] = [  # 指定群启用插件
    groupMessageRecorder,
    banImpl,
    helper,
    ShowStatus(),
    ServerMonitor(),  # 帮助
    PluginGroupManager(
        [
            AddPermission(),
            DelPermission(),
            ShowPermission(),
            AddGroupAdminToBotAdmin(),
            UserBan(banImpl),
            GetBanList(),
        ],
        "permission",
    ),  # 权限
    PluginGroupManager([AskFAQ(), MaintainFAQ(), HelpFAQ()], "faq"),  # 问答库与维护
    PluginGroupManager(
        [
            FireworksFace(),
            FirecrackersFace(),
            BasketballFace(),
            HotFace(),
            FlowerFace(),
            VegDog(),
            TouchFace(),
            BirthdayCake(),
            ff98sha(),
        ],
        "superemoji",
    ),  # 超级表情
    PluginGroupManager(
        [
            ShowMcStatus(),
            McStatusAddServer(),
            McStatusRemoveServer(),
            McStatusSetFooter(),
            McStatusRemoveFooter(),
        ],
        "mcs",
    ),  # MC服务器列表for MUA
    PluginGroupManager(
        [
            MuaQuery(),
            MuaAbstract(),
            MuaAnnHelper(),
            MuaAnnEditor(),
            MuaTokenBinder(),
            MuaTokenUnbinder(),
            MuaTokenEmpower(),
            MuaTokenLister(),
            MuaGroupBindTarget(),
            MuaGroupUnbindTarget(),
            MuaGroupAnnFilter(),
            PluginGroupManager([MuaNotice()], "muanotice"),
        ],
        "mua",
    ),  # MC高校联盟服务
    PluginGroupManager([BilibiliSubscribeHelper(), BilibiliSubscribe()], "bilibili"),
]
PrivatePluginList: List[StandardPlugin] = [  # 私聊启用插件
    helper,
    ShowStatus(),
    ServerMonitor(),
    LsGroup(),
    GroupApply(),
    PrivateControl(),
    helperForPrivateControl,
    MuaAbstract(),
    MuaQuery(),
    MuaAnnHelper(),
    MuaAnnEditor(),
    MuaTokenBinder(),
    MuaTokenUnbinder(),
    MuaTokenEmpower(),
    MuaTokenLister(),
]
GuildPluginList: List[GuildStandardPlugin] = []
GroupPokeList: List[PokeStandardPlugin] = [
    AutoRepoke(),  # 自动回复拍一拍
]
AddGroupVerifyPluginList: List[AddGroupStandardPlugin] = [
    AddGroupRecorder(),  # place this plugin to the first place
]
helper.updatePluginList(GroupPluginList, PrivatePluginList)
helperForPrivateControl.setPluginList(GroupPluginList)
app = Flask(__name__)


class NoticeType(IntEnum):
    NoProcessRequired = 0
    GroupMessageNoProcessRequired = 1
    GuildMessageNoProcessRequired = 2
    GocqHeartBeat = 5
    GroupMessage = 11
    GroupPoke = 12
    GroupRecall = 13
    GroupUpload = 14
    PrivateMessage = 21
    PrivatePoke = 22
    PrivateRecall = 23
    AddGroup = 31  # 有人要求加入自己的群
    AddPrivate = 32
    AddGroupInvite = 33  # 有人邀请自己加入新群
    GuildMessage = 41


def eventClassify(json_data: dict) -> NoticeType:
    """事件分类"""
    if (
        json_data["post_type"] == "meta_event"
        and json_data["meta_event_type"] == "heartbeat"
    ):
        return NoticeType.GocqHeartBeat
    elif json_data["post_type"] == "message":
        if json_data["message_type"] == "group":
            if json_data["group_id"] in APPLY_GROUP_ID:
                return NoticeType.GroupMessage
            else:
                return NoticeType.GroupMessageNoProcessRequired
        elif json_data["message_type"] == "private":
            return NoticeType.PrivateMessage
        elif json_data["message_type"] == "guild":
            if (json_data["guild_id"], json_data["channel_id"]) in APPLY_GUILD_ID:
                return NoticeType.GuildMessage
            else:
                return NoticeType.GuildMessageNoProcessRequired
    elif json_data["post_type"] == "notice":
        if json_data["notice_type"] == "notify":
            if json_data["sub_type"] == "poke":
                if json_data.get("group_id", None) in APPLY_GROUP_ID:
                    return NoticeType.GroupPoke
        elif json_data["notice_type"] == "group_recall":
            return NoticeType.GroupRecall
        elif json_data["notice_type"] == "group_upload":
            return NoticeType.GroupUpload
    elif json_data["post_type"] == "request":
        if json_data["request_type"] == "friend":
            return NoticeType.AddPrivate
        elif json_data["request_type"] == "group":
            if json_data["sub_type"] == "add":
                return NoticeType.AddGroup
            elif json_data["sub_type"] == "invite":
                return NoticeType.AddGroupInvite
    else:
        return NoticeType.NoProcessRequired


@app.route("/", methods=["POST"])
def post_data():
    # 获取事件上报
    data = request.get_json()
    # 筛选并处理指定事件
    flag = eventClassify(data)
    # 群消息处理
    if flag == NoticeType.GroupMessage:
        msg = data["message"].strip()
        for event in GroupPluginList:
            event: StandardPlugin
            try:
                if event.judgeTrigger(msg, data):
                    ret = event.executeEvent(msg, data)
                    if ret != None:
                        return ret
            except TypeError as e:
                warning("type error in main.py: {}\n\n{}".format(e, event))
    elif flag == NoticeType.GroupMessageNoProcessRequired:
        groupMessageRecorder.executeEvent(data["message"], data)
    elif flag == NoticeType.GroupRecall:
        for plugin in [groupMessageRecorder]:
            plugin.recallMessage(data)
    # 频道消息处理
    elif flag == NoticeType.GuildMessage:
        msg = data["message"].strip()
        for plugin in GuildPluginList:
            plugin: GuildStandardPlugin
            try:
                if plugin.judgeTrigger(msg, data):
                    ret = plugin.executeEvent(msg, data)
                    if ret != None:
                        return ret
            except TypeError as e:
                warning("type error in main.py: {}\n\n{}".format(e, plugin))
            except BaseException as e:
                warning(
                    "base exception in main.py guild plugin: {}\n\n{}".format(e, plugin)
                )
    # 私聊消息处理
    elif flag == NoticeType.PrivateMessage:
        # print(data)
        msg = data["message"].strip()
        for event in PrivatePluginList:
            if event.judgeTrigger(msg, data):
                if event.executeEvent(msg, data) != None:
                    break

    elif flag == NoticeType.AddGroup:
        for p in AddGroupVerifyPluginList:
            if p.judgeTrigger(data):
                if p.addGroupVerication(data) != None:
                    break
    # 上传文件处理
    elif flag == NoticeType.GroupUpload:
        for event in []:
            event.uploadFile(data)
    # 群内拍一拍回拍
    elif flag == NoticeType.GroupPoke:
        for p in GroupPokeList:
            if p.judgeTrigger(data):
                if p.pokeMessage(data) != None:
                    break

    # 自动加好友
    elif flag == NoticeType.AddPrivate:
        set_friend_add_request(data["flag"], True)
    # 自动通过加群邀请
    elif flag == NoticeType.AddGroupInvite:
        set_group_add_request(data["flag"], data["sub_type"], True)
    elif flag == NoticeType.GocqHeartBeat:
        gocqWatchDog.feed()
    return "OK"


def initCheck():
    # do some check
    for p in GroupPluginList:
        infoDict = p.getPluginInfo()
        assert (
            "name" in infoDict.keys()
            and "description" in infoDict.keys()
            and "commandDescription" in infoDict.keys()
            and "usePlace" in infoDict.keys()
        )
        if "group" not in infoDict["usePlace"]:
            print("plugin [{}] can not be used in group talk!".format(infoDict["name"]))
            exit(1)
    for p in PrivatePluginList:
        infoDict = p.getPluginInfo()
        assert (
            "name" in infoDict.keys()
            and "description" in infoDict.keys()
            and "commandDescription" in infoDict.keys()
            and "usePlace" in infoDict.keys()
        )
        if "private" not in infoDict["usePlace"]:
            print(
                "plugin [{}] can not be used in private talk!".format(infoDict["name"])
            )
            exit(1)
    gocqWatchDog.start()


if __name__ == "__main__":
    initCheck()
    app.run(host="127.0.0.1", port=5701)
