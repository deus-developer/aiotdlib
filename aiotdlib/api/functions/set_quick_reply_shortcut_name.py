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
class SetQuickReplyShortcutName(BaseObject):
    """
    Changes name of a quick reply shortcut

    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    :param name: New name for the shortcut. Use checkQuickReplyShortcutName to check its validness
    :type name: :class:`String`
    """

    ID: typing.Literal["setQuickReplyShortcutName"] = field(
        default="setQuickReplyShortcutName", metadata={"alias": "@type"}
    )
    shortcut_id: Int32
    name: String
