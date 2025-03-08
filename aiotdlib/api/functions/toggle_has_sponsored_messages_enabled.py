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
class ToggleHasSponsoredMessagesEnabled(BaseObject):
    """
    Toggles whether the current user has sponsored messages enabled. The setting has no effect for users without Telegram Premium for which sponsored messages are always enabled

    :param has_sponsored_messages_enabled: Pass true to enable sponsored messages for the current user; false to disable them
    :type has_sponsored_messages_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleHasSponsoredMessagesEnabled"] = field(
        default="toggleHasSponsoredMessagesEnabled", metadata={"alias": "@type"}
    )
    has_sponsored_messages_enabled: Bool = field(default=False)
