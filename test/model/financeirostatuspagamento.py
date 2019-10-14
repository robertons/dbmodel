#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroStatusPagamento(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def fin_status_pagamento(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_status_pagamento", reference="id")
	def acompanhantes_anuncios(self):pass

	@ObjectList(name="AcompanhanteCaseiraAdicional", key="id_status_pagamento", reference="id")
	def acompanhantes_caseiras_adicionais(self):pass

	@ObjectList(name="AcompanhanteCaseiraVip", key="id_status_pagamento", reference="id")
	def acompanhantes_caseiras_vips(self):pass

	@ObjectList(name="AcompanhanteCompra", key="id_status_pagamento", reference="id")
	def acompanhantes_compras(self):pass

	@ObjectList(name="AcompanhanteDestaque", key="id_status_pagamento", reference="id")
	def acompanhantes_destaques(self):pass

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_status_pagamento", reference="id")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="Financeiro", key="id_status_pagamento", reference="id")
	def financeiros(self):pass