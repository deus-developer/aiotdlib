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
class SetDatabaseEncryptionKey(BaseObject):
    """
    Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain

    :param new_encryption_key: New encryption key
    :type new_encryption_key: :class:`Bytes`
    """

    ID: typing.Literal["setDatabaseEncryptionKey"] = field(
        default="setDatabaseEncryptionKey", metadata={"alias": "@type"}
    )
    new_encryption_key: Bytes
