#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime

sys.path.append('/Users/roberto/projects/dbmodel')
import dbmodel

def main(arg):
    dbmodel.Make(dir = os.path.dirname(os.path.abspath(__file__)), db_user="root", db_password="", db_host="localhost", db_port=3306, db_database="ilhadoprazer")
    #dbmodel.Make(dir = os.path.dirname(os.path.abspath(__file__)), db_user="idp_master", db_password="aWkqH2MJFhCspZFV4m3JugUnnu", db_host="idp-instance.celwa7bjtmnw.us-east-2.rds.amazonaws.com", db_port=3306, db_database="ilhadoprazer")

if __name__ == "__main__":
    main(sys.argv)
