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
    db = dbmodel.Connection(db_user="idp_master", db_password="aWkqH2MJFhCspZFV4m3JugUnnu", db_host="idp-instance.celwa7bjtmnw.us-east-2.rds.amazonaws.com", db_port=3306, db_database="ilhadoprazer")

    #LOCAL
    #db = dbmodel.Connection(db_user="root", db_password="", db_host="localhost", db_port=3306, db_database="ilhadoprazer")

    lista = db.acompanhantes_avaliacoes.include("acompanhantes_avaliacoes_respostas").join("acompanhantes").where("acompanhantes.aco_publicada=1, acompanhantes_avaliacoes.ava_aprovado=1, acompanhantes_avaliacoes.id_acompanhante_avaliacao IS NULL, acompanhantes_avaliacoes_respostas.ava_aprovado=1").select("acompanhantes_avaliacoes.*, acompanhantes_avaliacoes_respostas.*").orderby("id_acompanhante ASC, ava_likes DESC, acompanhantes_avaliacoes_respostas.ava_ordem_resposta ASC, acompanhantes_avaliacoes_respostas.ava_data ASC").all

    for item in lista:
        print(item.ava_comentario)
        for resp in item.acompanhantes_avaliacoes_respostas:
            print(resp.ava_comentario)
    #print(lista)

    db.close()

if __name__ == "__main__":
    main(sys.argv)
