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
class DeleteBusinessChatLink(BaseObject):
    """
    Deletes a business chat link of the current account

    :param link: The link to delete
    :type link: :class:`String`
    """

    ID: typing.Literal["deleteBusinessChatLink"] = field(default="deleteBusinessChatLink", metadata={"alias": "@type"})
    link: String
