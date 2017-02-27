#!/usr/bin/env python3
# Copyright (c) 2017 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from framework.build.bdb import BerkeleyDb


bdb = BerkeleyDb("/tmp/bdb-test/")

bdb.build()
