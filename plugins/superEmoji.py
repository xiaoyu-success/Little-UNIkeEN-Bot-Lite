from typing import Union, Any
from utils.basicEvent import *
from utils.standardPlugin import StandardPlugin


class FireworksFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["放个烟花", "烟花"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=333,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "FireworksFace",
            "description": "烟花",
            "commandDescription": "放个烟花/烟花",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class FirecrackersFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["点个鞭炮", "鞭炮"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=137,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "FirecrackersFace",
            "description": "鞭炮",
            "commandDescription": "点个鞭炮/鞭炮",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class BasketballFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["投个篮球", "投篮"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=114,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "BasketballFace",
            "description": "投篮",
            "commandDescription": "投个篮球/投篮",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class HotFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["热死了", "好热", "太热了"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=340,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "HotFace",
            "description": "热化了",
            "commandDescription": "热死了/好热/太热了",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class FlowerFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["花朵脸"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=337,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "FlowerFace",
            "description": "花朵脸",
            "commandDescription": "花朵脸",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class TouchFace(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["戳一戳"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=181,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "TouchFace",
            "description": "戳一戳",
            "commandDescription": "戳一戳",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class VegDog(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["菜狗"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=317,type=sticker]", data["message_type"])
        send(target, "杂鱼~", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "VegDog",
            "description": "菜狗",
            "commandDescription": "菜狗",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class BirthdayCake(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["生日快乐", "生快"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=53,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "BirthdayCake",
            "description": "生日蛋糕",
            "commandDescription": "生日快乐/生快",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class GoHome(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["我想回家", "呜呜呜"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(target, "[CQ:face,id=5,type=sticker]", data["message_type"])
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "GoHome",
            "description": "我想回家",
            "commandDescription": "我想回家/呜呜呜",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }


class ff98sha(StandardPlugin):
    def judgeTrigger(self, msg: str, data: Any) -> bool:
        return msg in ["ff98sha", "\\ff98sha/"]

    def executeEvent(self, msg: str, data: Any) -> Union[None, str]:
        target = (
            data["group_id"] if data["message_type"] == "group" else data["user_id"]
        )
        send(
            target,
            "[CQ:image,file=ee524565c508fe9582e698aeecf34de0.image,subType=1,url=https://gchat.qpic.cn/gchatpic_new/1241836708/796846995-2532198366-EE524565C508FE9582E698AEECF34DE0/0?term=2&amp;is_origin=0]",
            data["message_type"],
        )
        return "OK"

    def getPluginInfo(
            self,
    ) -> dict:
        return {
            "name": "ff98sha",
            "description": "ff98sha是我男神",
            "commandDescription": "ff98sha,\\ff98sha/",
            "usePlace": ["group", "private"],
            "showInHelp": True,
            "pluginConfigTableNames": [],
            "version": "1.0.0",
            "author": "Unicorn",
        }
