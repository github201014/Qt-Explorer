from enum import Enum
class LanguageEnum(Enum):
    zh_CN = 0
    zh_TW = 1
    en_US = 2

class StatusEnum(Enum):
    MAIN_NO_WINDOW_YES = 0
    MAIN_NO_WINDOW_NO = 1
    MAIN_YES_WINDOW_YES = 2