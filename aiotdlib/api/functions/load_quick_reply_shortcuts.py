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
class LoadQuickReplyShortcuts(BaseObject):
    """
    Loads quick reply shortcuts created by the current user. The loaded data will be sent through updateQuickReplyShortcut and updateQuickReplyShortcuts
    """

    ID: typing.Literal["loadQuickReplyShortcuts"] = field(
        default="loadQuickReplyShortcuts", metadata={"alias": "@type"}
    )
