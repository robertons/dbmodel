#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAtendimento(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Decimal(precision = 19, scale=2)
	def atd_valor(self): pass

	@Int(precision = 3, scale=0)
	def atd_massagem(self): pass

	@Int(precision = 3, scale=0)
	def atd_vaginal(self): pass

	@Int(precision = 3, scale=0)
	def atd_oral(self): pass

	@Int(precision = 3, scale=0)
	def atd_anal(self): pass

	@Int(precision = 3, scale=0)
	def atd_grupal(self): pass

	@Int(precision = 3, scale=0)
	def atd_beijo_na_boca(self): pass

	@Int(precision = 3, scale=0)
	def atd_fetiches(self): pass

	@Int(precision = 3, scale=0)
	def atd_dominacao(self): pass

	@Int(precision = 3, scale=0)
	def atd_inversao_de_papeis(self): pass

	@Int(precision = 3, scale=0)
	def atd_beijo_grego(self): pass

	@Int(precision = 3, scale=0)
	def atd_striptease(self): pass

	@Int(precision = 3, scale=0)
	def atd_chuva_dourada(self): pass

	@Int(precision = 3, scale=0)
	def atd_chuva_negra(self): pass

	@Int(precision = 3, scale=0)
	def atd_bdsm(self): pass

	@Int(precision = 3, scale=0)
	def atd_festas_eventos(self): pass

	@Int(precision = 3, scale=0)
	def atd_local_atendimento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_atendimento(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	@Object(name="AcompanhanteAtendimentoTipo", key="id", reference="id_tipo_atendimento")
	def acompanhantes_atendimentos_tipos(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteNotificacao", key="id_atendimento_acompanhante", reference="id")
	def acompanhantes_notificacoes(self):pass