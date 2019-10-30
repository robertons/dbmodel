#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteNotificacao(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@DateTime()
	def not_data(self): pass

	@String(max=150)
	def not_texto(self): pass

	@String(max=150)
	def not_texto_acao(self): pass

	@Int(precision = 3, scale=0)
	def not_ativa(self): pass

	@DateTime()
	def not_data_criacao(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_atendimento_acompanhante(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_estado(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_cidade(self): pass

	@Int(precision = 10, scale=0)
	def not_desconto(self): pass

	# One-to-One

	@Object(name="Cidade", key="id", reference="id_cidade", table="cidades")
	def cidades(self):pass

	@Object(name="AcompanhanteAtendimento", key="id", reference="id_atendimento_acompanhante", table="acompanhantes_atendimentos")
	def acompanhantes_atendimentos(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	@Object(name="Estado", key="id", reference="id_estado", table="estados")
	def estados(self):pass