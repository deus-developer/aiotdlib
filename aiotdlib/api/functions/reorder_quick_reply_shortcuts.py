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
class ReorderQuickReplyShortcuts(BaseObject):
    """
    Changes the order of quick reply shortcuts

    :param shortcut_ids: The new order of quick reply shortcuts
    :type shortcut_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["reorderQuickReplyShortcuts"] = field(
        default="reorderQuickReplyShortcuts", metadata={"alias": "@type"}
    )
    shortcut_ids: Vector[Int32]
