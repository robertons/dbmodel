#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime

sys.path.append('/Users/roberto/projects/dbmodel')

import dbmodel

def main(arg):
    #AWS
    #db = dbmodel.Connection(db_user="idp_master", db_password="aWkqH2MJFhCspZFV4m3JugUnnu", db_host="idp-instance.celwa7bjtmnw.us-east-2.rds.amazonaws.com", db_port=3306, db_database="ilhadoprazer")

    #LOCAL
    db = dbmodel.Connection(db_user="root", db_password="", db_host="localhost", db_port=3306, db_database="ilhadoprazer")

    lista = db.acompanhantes.join("sexos").include("acompanhantes_atendimentos").select("acompanhantes.aco_nome, sexos.sexo_nome, acompanhantes_atendimentos.atd_valor").limit(1100,10).all
    #print(lista.toJSON())
    #lista[3].aco_nome = "Teste"
    for item in lista:
        print(item.acompanhantes_atendimentos[0].atd_valor)
        #pass
        #print(item.toJSON())
    db.close()

if __name__ == "__main__":
    main(sys.argv)
