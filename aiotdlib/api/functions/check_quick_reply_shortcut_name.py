# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CheckQuickReplyShortcutName(BaseObject):
    """
    Checks validness of a name for a quick reply shortcut. Can be called synchronously

    :param name: The name of the shortcut; 1-32 characters
    :type name: :class:`String`
    """

    ID: typing.Literal["checkQuickReplyShortcutName"] = field(
        default="checkQuickReplyShortcutName", metadata={"alias": "@type"}
    )
    name: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 32})
