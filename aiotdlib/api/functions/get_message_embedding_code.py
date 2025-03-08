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
class GetMessageEmbeddingCode(BaseObject):
    """
    Returns an HTML code for embedding the message. Available only if messageProperties.can_get_embedding_code

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param for_album: Pass true to return an HTML code for embedding of the whole media album
    :type for_album: :class:`Bool`
    """

    ID: typing.Literal["getMessageEmbeddingCode"] = field(
        default="getMessageEmbeddingCode", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_id: Int53
    for_album: Bool = field(default=False)
