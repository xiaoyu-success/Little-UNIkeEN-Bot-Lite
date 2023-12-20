from PIL import Image, ImageDraw, ImageFont
import os
from enum import IntEnum


class BACKEND_TYPE(IntEnum):
    GOCQHTTP = 1
    LAGRANGE = 2


BACKEND = BACKEND_TYPE.LAGRANGE

if BACKEND == BACKEND_TYPE.GOCQHTTP:
    HTTP_URL = "http://127.0.0.1:5701"
elif BACKEND == BACKEND_TYPE.LAGRANGE:
    HTTP_URL = "ws://127.0.0.1:5705"  # Lagrange
else:
    assert False

# BOT_SELF_QQ=get_login_info()['user_id']
BOT_SELF_QQ = None  # bot自己qq号是多少
assert BOT_SELF_QQ != None, 'BOT的QQ号是多少'

VERSION_TXT = """version：muaLite版本，NJFU基于Little-UNIkeEN-Bot的muaLTS分支维护的精简版本
本版本更新内容见GitHub(可能需要科学上网)： https://github.com/xiaoyu-success/Little-UNIkeEN-Bot-Lite/
国内自建Gitlab：https://codeserver.youkeda.com/xiaoyu01/little-unikeen-bot-lite/"""

sqlConfig = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': '' # bot的sql密码是多少
}
assert sqlConfig.get('passwd', None) != None, '请填入bot sql的密码'

# 根路径与资源路径
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))[:-6]
FONTS_PATH = 'resources/fonts'
IMAGES_PATH = 'resources/images/'
SAVE_TMP_PATH = 'data/tmp'
os.makedirs(SAVE_TMP_PATH, exist_ok=True)

# 画图颜色常量与文字
BACK_CLR = {'r':(255, 232, 236, 255),'g':(219, 255, 228, 255),'h':(234, 234, 234, 255),'o':(254, 232, 199, 255)}
FONT_CLR = {'r':(221, 0, 38, 255),'g':(0, 191, 48, 255),'h':(64, 64, 64, 255),'o':(244, 149 ,4, 255)}
font_syht_m = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Normal.otf'), 18)
font_syht_mm = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Normal.otf'), 24)
font_syht_ml = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Normal.otf'), 32)
font_syhtmed_32 = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Medium.otf'), 32)
font_syhtmed_24 = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Medium.otf'), 24)
font_syhtmed_18 = ImageFont.truetype(os.path.join(FONTS_PATH, 'SourceHanSansCN-Medium.otf'), 18)
font_hywh_85w = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 40)
font_hywh_85w_xs = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 18)
font_hywh_85w_s = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 20)
font_hywh_85w_mms = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 25)
font_hywh_85w_ms = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 30)
font_hywh_85w_l = ImageFont.truetype(os.path.join(FONTS_PATH, '汉仪文黑.ttf'), 55)
font_sg_emj = ImageFont.truetype(os.path.join(FONTS_PATH, 'seguiemj.ttf'), 55)
font_sg_emj_l = ImageFont.truetype(os.path.join(FONTS_PATH, 'seguiemj.ttf'), 75)
