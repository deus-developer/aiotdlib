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
class SearchFileDownloads(BaseObject):
    """
    Searches for files in the file download list or recently downloaded files from the list

    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of files to be returned
    :type limit: :class:`Int32`
    :param query: Query to search for; may be empty to return all downloaded files
    :type query: :class:`String`
    :param only_active: Pass true to search only for active downloads, including paused
    :type only_active: :class:`Bool`
    :param only_completed: Pass true to search only for completed downloads
    :type only_completed: :class:`Bool`
    """

    ID: typing.Literal["searchFileDownloads"] = field(default="searchFileDownloads", metadata={"alias": "@type"})
    offset: String
    limit: Int32
    query: String = field(default="")
    only_active: Bool = field(default=False)
    only_completed: Bool = field(default=False)
