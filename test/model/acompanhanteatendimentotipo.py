#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAtendimentoTipo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def atd_descricao(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteAtendimento", key="id_tipo_atendimento", reference="id", table="acompanhantes_atendimentos")
	def acompanhantes_atendimentos(self):pass