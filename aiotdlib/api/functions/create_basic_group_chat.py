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
class CreateBasicGroupChat(BaseObject):
    """
    Returns an existing chat corresponding to a known basic group

    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`Int53`
    :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
    :type force: :class:`Bool`
    """

    ID: typing.Literal["createBasicGroupChat"] = field(default="createBasicGroupChat", metadata={"alias": "@type"})
    basic_group_id: Int53
    force: Bool = field(default=False)
