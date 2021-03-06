# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com.
# All rights reserved.
#
# db/sqlsqlite.py
#

from .sqlnone import SqlNone

from ppmessage.core.constant import SQL
from ppmessage.core.singleton import singleton
from ppmessage.core.utils.config import get_config_sqlite

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.pool import Pool

from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy import create_engine

from sqlite3 import dbapi2 as sqlite

import logging
import traceback

class SqlInstance(SqlNone):

    def __init__(self):
        _sqlite = get_config_sqlite()
        _dbpath = None
        if _sqlite != None:
            _dbpath = _sqlite.get("db_path")
        if _dbpath == None:
            _dbpath = "/usr/local/var/db/sqlite/ppmessage.db"
        self.dbpath = _dbpath
        super(SqlInstance, self).__init__()
        return

    def name(self):
        return SQL.SQLITE
    
    def createEngine(self):
        _dbstring = "sqlite+pysqlite:///%s" % self.dbpath
        if self.dbengine == None:
            _engine = create_engine(_dbstring, module=sqlite)
            self.dbengine = _engine
        return self.dbengine
