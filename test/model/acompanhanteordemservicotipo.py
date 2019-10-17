#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteOrdemServicoTipo(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(not_null=True, max=45)
	def ord_srv_nome(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteOrdemServico", key="id_acompanhante_ordem_servico_tipo", reference="id", table="acompanhantes_ordens_servicos")
	def acompanhantes_ordens_servicos(self):pass