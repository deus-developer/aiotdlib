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
class ToggleGiftIsSaved(BaseObject):
    """
    Toggles whether a gift is shown on the current user's or the channel's profile page; requires can_post_messages administrator right in the chat

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    :param is_saved: Pass true to display the gift on the user's or the channel's profile page; pass false to remove it from the profile page
    :type is_saved: :class:`Bool`
    """

    ID: typing.Literal["toggleGiftIsSaved"] = field(default="toggleGiftIsSaved", metadata={"alias": "@type"})
    received_gift_id: String
    is_saved: Bool = field(default=False)
