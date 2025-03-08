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
class ClearImportedContacts(BaseObject):
    """
    Clears all imported contacts, contact list remains unchanged
    """

    ID: typing.Literal["clearImportedContacts"] = field(default="clearImportedContacts", metadata={"alias": "@type"})
