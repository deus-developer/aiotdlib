# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    Contact,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ImportContacts(BaseObject):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

    :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
    :type contacts: :class:`Vector[Contact]`
    """

    ID: typing.Literal["importContacts"] = field(default="importContacts", metadata={"alias": "@type"})
    contacts: Vector[Contact]
