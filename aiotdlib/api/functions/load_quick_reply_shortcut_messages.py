# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class LoadQuickReplyShortcutMessages(BaseObject):
    """
    Loads quick reply messages that can be sent by a given quick reply shortcut. The loaded messages will be sent through updateQuickReplyShortcutMessages

    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    """

    ID: typing.Literal["loadQuickReplyShortcutMessages"] = field(
        default="loadQuickReplyShortcutMessages", metadata={"alias": "@type"}
    )
    shortcut_id: Int32
