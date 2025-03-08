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
class RemoveContacts(BaseObject):
    """
    Removes users from the contact list

    :param user_ids: Identifiers of users to be deleted
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["removeContacts"] = field(default="removeContacts", metadata={"alias": "@type"})
    user_ids: Vector[Int53]
