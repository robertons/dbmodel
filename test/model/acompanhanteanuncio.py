#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteAnuncio(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_anuncio(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_status_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_forma_pagamento(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_tipo_desconto(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_servico(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_anuncio_status(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_financeiro(self): pass

	@DateTime(not_null=True)
	def anun_data(self): pass

	@DateTime(not_null=True)
	def anun_data_inicio(self): pass

	@DateTime(not_null=True)
	def anun_data_vencimento(self): pass

	@DateTime(not_null=True)
	def anun_data_limite_renovacao(self): pass

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

	@Int(not_null=True, precision = 10, scale=0)
	def anun_prazo(self): pass

	@String(max=65535)
	def anun_observacoes(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante")
	def acompanhantes(self):pass

	@Object(name="FinanceiroFormaPagamento", key="id", reference="id_forma_pagamento")
	def financeiros_formas_pagamentos(self):pass

	@Object(name="FinanceiroServico", key="id", reference="id_servico")
	def financeiros_servicos(self):pass

	@Object(name="FinanceiroStatusPagamento", key="id", reference="id_status_pagamento")
	def financeiros_status_pagamentos(self):pass

	@Object(name="AcompanhanteAnuncioStatus", key="id", reference="id_anuncio_status")
	def acompanhantes_anuncios_status(self):pass

	@Object(name="FinanceiroTipoDesconto", key="id", reference="id_tipo_desconto")
	def financeiros_tipos_descontos(self):pass

	@Object(name="AcompanhanteAnuncioTipo", key="id", reference="id_tipo_anuncio")
	def acompanhantes_anuncios_tipos(self):pass

	@Object(name="Financeiro", key="id", reference="id_financeiro")
	def financeiros(self):pass