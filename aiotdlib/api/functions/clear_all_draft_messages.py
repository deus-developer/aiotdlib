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
class ClearAllDraftMessages(BaseObject):
    """
    Clears message drafts in all chats

    :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
    :type exclude_secret_chats: :class:`Bool`
    """

    ID: typing.Literal["clearAllDraftMessages"] = field(default="clearAllDraftMessages", metadata={"alias": "@type"})
    exclude_secret_chats: Bool = field(default=False)
