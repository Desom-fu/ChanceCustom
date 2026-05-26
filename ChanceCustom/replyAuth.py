r"""
_________ ___________________ ____  __.
\_   ___ \\_   ___ \______   \    |/ _|
/    \  \//    \  \/|     ___/      <
\     \___\     \___|    |   |    |  \
 \______  /\______  /____|   |____|__ \
        \/        \/                 \/
@File      :   replyContent.py
@Author    :   Linnest
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2026, OlivOS-Team
@Desc      :   None
"""

import OlivOS
import ChanceCustom
from ChanceCustom.replyBase import CurryTemp
import re


def set_group_ban(
    plugin_event: OlivOS.API.Event,
    group_id: 'str|int',
    user_id: 'str|int',
    host_id: 'str|int|None' = None,
    duration: int = 1800,
):
    plugin_event.set_group_ban(group_id, user_id, host_id, duration=duration)


@CurryTemp
def set_group_ban_matcher(matched: 're.Match|dict', **kwargs):
    valDict = kwargs['valDict']
    groupDict = ChanceCustom.replyBase.getGroupDictInit(matched)
    resDict = {}

    ChanceCustom.replyBase.getNumRegTotal(resDict, '时间', 300, groupDict, valDict)
    ChanceCustom.replyBase.getNumRegTotal(resDict, 'QQ', valDict['defaultVal']['发送者QQ'], groupDict, valDict)

    try:
        set_group_ban(
            plugin_event=valDict['innerVal']['plugin_event'],
            group_id=valDict['defaultVal']['当前群号'],
            user_id=resDict['QQ'],
            duration=resDict['时间'],
        )
    except Exception:
        print('？', flush=True)
    return ''
