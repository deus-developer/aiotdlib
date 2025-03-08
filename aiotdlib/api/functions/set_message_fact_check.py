# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    FormattedText,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetMessageFactCheck(BaseObject):
    """
    Changes the fact-check of a message. Can be only used if messageProperties.can_set_fact_check == true

    :param chat_id: The channel chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param text: New text of the fact-check; 0-getOption("fact_check_length_max") characters; pass null to remove it. Only Bold, Italic, and TextUrl entities with https://t.me/ links are supported, defaults to None
    :type text: :class:`FormattedText`, optional
    """

    ID: typing.Literal["setMessageFactCheck"] = field(default="setMessageFactCheck", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    text: typing.Optional[FormattedText] = field(default=None)
