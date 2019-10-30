#-*- coding: utf-8 -*-
from dbmodel.entity import *

class FinanceiroFormaPagamento(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@String(max=45)
	def fin_forma_pagamento(self): pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_forma_pagamento", reference="id", table="acompanhantes_anuncios")
	def acompanhantes_anuncios(self):pass

	@ObjectList(name="AcompanhanteCaseiraAdicional", key="id_forma_pagamento", reference="id", table="acompanhantes_caseiras_adicionais")
	def acompanhantes_caseiras_adicionais(self):pass

	@ObjectList(name="AcompanhanteCaseiraVip", key="id_forma_pagamento", reference="id", table="acompanhantes_caseiras_vips")
	def acompanhantes_caseiras_vips(self):pass

	@ObjectList(name="AcompanhanteDestaque", key="id_forma_pagamento", reference="id", table="acompanhantes_destaques")
	def acompanhantes_destaques(self):pass

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_forma_pagamento", reference="id", table="acompanhantes_ensaios_edicoes")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="Financeiro", key="id_forma_pagamento", reference="id", table="financeiros")
	def financeiros(self):pass