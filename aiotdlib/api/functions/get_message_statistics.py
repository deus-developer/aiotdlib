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
class GetMessageStatistics(BaseObject):
    """
    Returns detailed statistics about a message. Can be used only if messageProperties.can_get_statistics == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param is_dark: Pass true if a dark theme is used by the application
    :type is_dark: :class:`Bool`
    """

    ID: typing.Literal["getMessageStatistics"] = field(default="getMessageStatistics", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    is_dark: Bool = field(default=False)
