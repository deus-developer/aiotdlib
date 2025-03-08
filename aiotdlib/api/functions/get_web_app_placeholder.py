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
class GetWebAppPlaceholder(BaseObject):
    """
    Returns a default placeholder for Web Apps of a bot; this is an offline request. Returns a 404 error if the placeholder isn't known

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getWebAppPlaceholder"] = field(default="getWebAppPlaceholder", metadata={"alias": "@type"})
    bot_user_id: Int53
