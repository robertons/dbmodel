#-*- coding: utf-8 -*-
from dbmodel.entity import *

class AcompanhanteOrdemServico(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante(self): pass

	@DateTime()
	def ord_data(self): pass

	@DateTime()
	def ord_data_realizacao(self): pass

	@String(max=65535)
	def ord_descricao(self): pass

	@Int(precision = 3, scale=0)
	def ord_finalizado(self): pass

	@Int(precision = 3, scale=0)
	def ord_visualizado(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_usuario_criador(self): pass

	@Int(fk=True, precision = 10, scale=0)
	def id_usuario_realizador(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_acompanhante_ordem_servico_tipo(self): pass

	# One-to-One

	@Object(name="Acompanhante", key="id", reference="id_acompanhante", table="acompanhantes")
	def acompanhantes(self):pass

	@Object(name="Usuario", key="id", reference="id_usuario_realizador", table="usuarios")
	def usuarios(self):pass

	@Object(name="AcompanhanteOrdemServicoTipo", key="id", reference="id_acompanhante_ordem_servico_tipo", table="acompanhantes_ordens_servicos_tipos")
	def acompanhantes_ordens_servicos_tipos(self):pass

	@Object(name="Usuario", key="id", reference="id_usuario_criador", table="usuarios")
	def usuarios(self):pass