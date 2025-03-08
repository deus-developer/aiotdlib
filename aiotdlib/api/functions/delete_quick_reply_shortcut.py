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
class DeleteQuickReplyShortcut(BaseObject):
    """
    Deletes a quick reply shortcut

    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    """

    ID: typing.Literal["deleteQuickReplyShortcut"] = field(
        default="deleteQuickReplyShortcut", metadata={"alias": "@type"}
    )
    shortcut_id: Int32
