#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
from enum import IntEnum
#
#  * Enumerates how data is access on read or write.
#
class VariableAccessSpecification(IntEnum):
    #
    # Read data using SN.
    #
    VARIABLE_NAME = 2

    #
    # Get data using parameterized access.
    #
    PARAMETERISED_ACCESS = 4

    #
    # Get next block.
    #
    BLOCK_NUMBER_ACCESS = 5

    #
    # Read data as blocks.
    #
    READ_DATA_BLOCK_ACCESS = 6

    #
    # Write data as blocks.
    #
    WRITE_DATA_BLOCK_ACCESS = 7
