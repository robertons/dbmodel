#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteCompra(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@DateTime(not_null=True)
	def compra_data(self): pass

	@String(max=100)
	def compra_wc_order_id(self): pass

	@String(max=100)
	def compra_wc_payment_id(self): pass

	@String(max=100)
	def compra_wc_customer_id(self): pass

	@String(max=65535)
	def compra_wc_cc_hash(self): pass

	@String(max=45)
	def compra_wc_holder_name(self): pass

	@DateTime()
	def compra_wc_holder_birthday(self): pass

	@String(max=11)
	def compra_wc_holder_phone(self): pass

	@String(max=11)
	def compra_wc_holder_cpf(self): pass

	@String(max=155)
	def compra_wc_status(self): pass

	@String(max=155)
	def fin_descricao(self): pass

	@Decimal(precision = 19, scale=2)
	def fin_valor_servico(self): pass

	@Decimal(precision = 19, scale=2)
	def fin_tx_servico(self): pass

	@Decimal(precision = 19, scale=2)
	def fin_desconto(self): pass

	@Decimal(precision = 19, scale=2)
	def fin_valor_a_pagar(self): pass

	@Decimal(precision = 19, scale=2)
	def fin_valor_pago(self): pass

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

	@Object(name="FinanceiroStatusPagamento", key="id", reference="id_status_pagamento", table="financeiros_status_pagamentos")
	def financeiros_status_pagamentos(self):pass

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	@Object(name="Financeiro", key="id", reference="id_financeiro", table="financeiros")
	def financeiros(self):pass

	@Object(name="FinanceiroTipoDesconto", key="id", reference="id_tipo_desconto", table="financeiros_tipos_descontos")
	def financeiros_tipos_descontos(self):pass

	@Object(name="FinanceiroFormaPagamento", key="id", reference="id_forma_pagamento", table="financeiros_formas_pagamentos")
	def financeiros_formas_pagamentos(self):pass

	@Object(name="FinanceiroServico", key="id", reference="id_servico", table="financeiros_servicos")
	def financeiros_servicos(self):pass