#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Financeiro(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_servico(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_forma_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_status_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_desconto(self): pass

	@DateTime()
	def fin_data(self): pass

	@String(max=155)
	def fin_descricao(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_valor_servico(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_tx_servico(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_desconto(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_valor_a_pagar(self): pass

	@Decimal(not_null=True, precision = 19, scale=2)
	def fin_valor_pago(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def fin_rps_emitido(self): pass

	@DateTime()
	def fin_rps_data(self): pass

	# One-to-One

	@Object(name="FinanceiroTipoDesconto", key="id", reference="id_tipo_desconto")
	def financeiros_tipos_descontos(self):pass

	@Object(name="FinanceiroFormaPagamento", key="id", reference="id_forma_pagamento")
	def financeiros_formas_pagamentos(self):pass

	@Object(name="FinanceiroServico", key="id", reference="id_servico")
	def financeiros_servicos(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	@Object(name="FinanceiroStatusPagamento", key="id", reference="id_status_pagamento")
	def financeiros_status_pagamentos(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteAnuncio", key="id_financeiro", reference="id")
	def acompanhantes_anuncios(self):pass

	@ObjectList(name="AcompanhanteCaseiraAdicional", key="id_financeiro", reference="id")
	def acompanhantes_caseiras_adicionais(self):pass

	@ObjectList(name="AcompanhanteCaseiraVip", key="id_financeiro", reference="id")
	def acompanhantes_caseiras_vips(self):pass

	@ObjectList(name="AcompanhanteCompra", key="id_financeiro", reference="id")
	def acompanhantes_compras(self):pass

	@ObjectList(name="AcompanhanteDestaque", key="id_financeiro", reference="id")
	def acompanhantes_destaques(self):pass

	@ObjectList(name="AcompanhanteEnsaioEdicao", key="id_financeiro", reference="id")
	def acompanhantes_ensaios_edicoes(self):pass

	@ObjectList(name="FinanceiroLoteRpsRecibo", key="id_financeiro", reference="id")
	def financeiros_lotes_rps_recibos(self):pass