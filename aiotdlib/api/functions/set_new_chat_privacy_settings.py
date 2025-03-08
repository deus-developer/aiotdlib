# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    NewChatPrivacySettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetNewChatPrivacySettings(BaseObject):
    """
    Changes privacy settings for new chat creation; can be used only if getOption("can_set_new_chat_privacy_settings")

    :param settings: New settings
    :type settings: :class:`NewChatPrivacySettings`
    """

    ID: typing.Literal["setNewChatPrivacySettings"] = field(
        default="setNewChatPrivacySettings", metadata={"alias": "@type"}
    )
    settings: NewChatPrivacySettings
