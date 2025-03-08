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
class ToggleChatFolderTags(BaseObject):
    """
    Toggles whether chat folder tags are enabled

    :param are_tags_enabled: Pass true to enable folder tags; pass false to disable them
    :type are_tags_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleChatFolderTags"] = field(default="toggleChatFolderTags", metadata={"alias": "@type"})
    are_tags_enabled: Bool = field(default=False)
