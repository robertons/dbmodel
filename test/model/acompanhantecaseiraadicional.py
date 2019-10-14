#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteCaseiraAdicional(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@DateTime(not_null=True)
	def adi_data(self): pass

	@Int(not_null=True, precision = 10, scale=0)
	def adi_dias(self): pass

	@String(not_null=True, max=45)
	def adi_tipo(self): pass

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

	@Int(precision = 10, scale=0)
	def id_primeiro_dia(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_status_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_forma_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_desconto(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_servico(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_financeiro(self): pass

	# One-to-One

	@Object(name="FinanceiroFormaPagamento", key="id", reference="id_forma_pagamento")
	def financeiros_formas_pagamentos(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	@Object(name="FinanceiroServico", key="id", reference="id_servico")
	def financeiros_servicos(self):pass

	@Object(name="FinanceiroStatusPagamento", key="id", reference="id_status_pagamento")
	def financeiros_status_pagamentos(self):pass

	@Object(name="FinanceiroTipoDesconto", key="id", reference="id_tipo_desconto")
	def financeiros_tipos_descontos(self):pass

	@Object(name="Financeiro", key="id", reference="id_financeiro")
	def financeiros(self):pass