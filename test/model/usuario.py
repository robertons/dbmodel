#-*- coding: utf-8 -*-
from dbmodel.entity import *

class Usuario(Entity):

	__primary_key__ = ['id']

	# FIELDS

	@Int(pk=True, auto_increment=True, not_null=True, precision = 10, scale=0)
	def id(self): pass

	@Int(fk=True, not_null=True, precision = 10, scale=0)
	def id_perfil(self): pass

	@String(not_null=True, max=45)
	def usu_nome(self): pass

	@String(not_null=True, max=45)
	def usu_email(self): pass

	@String(fk=True, not_null=True, max=45)
	def usu_senha(self): pass

	@String(fk=True, not_null=True, max=20)
	def usu_login(self): pass

	@DateTime(not_null=True)
	def usu_last_login(self): pass

	@Int(not_null=True, precision = 3, scale=0)
	def usu_active(self): pass

	# One-to-One

	@Object(name="Perfil", key="id", reference="id_perfil")
	def perfis(self):pass

	# One-to-many

	@ObjectList(name="AcompanhanteFotoCaseira", key="id_usuario", reference="id")
	def acompanhantes_fotos_caseiras(self):pass

	@ObjectList(name="AcompanhanteLog", key="id_usuario", reference="id")
	def acompanhantes_logs(self):pass

	@ObjectList(name="AcompanhanteOrdemServico", key="id_usuario_criador", reference="id")
	def acompanhantes_ordens_servicos(self):pass

	@ObjectList(name="AcompanhanteOrdemServico", key="id_usuario_realizador", reference="id")
	def acompanhantes_ordens_servicos(self):pass

	@ObjectList(name="Log", key="id_usuario", reference="id")
	def logs(self):pass

	@ObjectList(name="UsuarioDepartamento", key="id_usuario", reference="id")
	def usuarios_departamentos(self):pass

	@ObjectList(name="UsuarioModulo", key="id_usuario", reference="id")
	def usuarios_modulos(self):pass