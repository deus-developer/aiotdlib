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
class DeleteAllCallMessages(BaseObject):
    """
    Deletes all call messages

    :param revoke: Pass true to delete the messages for all users
    :type revoke: :class:`Bool`
    """

    ID: typing.Literal["deleteAllCallMessages"] = field(default="deleteAllCallMessages", metadata={"alias": "@type"})
    revoke: Bool = field(default=False)
