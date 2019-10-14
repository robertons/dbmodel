# -*- coding: utf-8 -*-

import sys
import re

from dbmodel.utils.inflector import Inflector, Portugues
from dbmodel.context.database import DataBase
from dbmodel.entity.datatype import ListType
from dbmodel.entity.entity import EntityStatus

sql_operators = [ '!=', '>=','>','<=','<','=', 'NOT IS', 'IS', 'NOT LIKE', 'LIKE', ' ']
relational_types = ["Object" , "ObjectList"]

class Connection():

    def __init__(self, db_user=None, db_password=None, db_host=None, db_port=None, db_database=None, db_ssl=False, db_ssl_ca=None, db_ssl_cert=None, db_ssl_key=None):
        try:
            self._inflector = Inflector(Portugues)
            self._db = DataBase(db_user, db_password, db_host, db_port, db_database, db_ssl,db_ssl_ca, db_ssl_cert, db_ssl_key)
            self._commit = []
        except Exception as e:
            raise e

    def close(self):
        self._db.close()

    #VERIFICA SE O ATRIBUTO INFORMADO É UM METODO EXISTENTE SE NÃO FOR TRATA PARA VERIFICAR SE É UMA TABELA
    def __getattr__(self, name):
        try:
            if not "_table" in self.__dir__():
                self._table = name
                self._select = None
                self._where = None
                self._having = None
                self._orhaving = None
                self._orwhere = None
                self._order_by = None
                self._group_by = None
                self._limit = None
                self._left = None
                classname =  self._inflector.classify(name)
                self._class = getattr(__import__('model.{0}'.format(classname.lower()), fromlist=[classname]), classname)
            else:
                return None
            return self
        except Exception as e:
            raise  e

    # VERIFICAÇÃO SE HÁ OPERADOR NO CAMPO
    def __operator_check(self, field):
        exists_operator = [operator in field for operator in sql_operators]
        if any(exists_operator):
            field = field.strip().split(sql_operators[exists_operator.index(True)])
            field[0] = field[0].strip()
            field.insert(1, sql_operators[exists_operator.index(True)])
        return field

    def __valid_table(self):
        if not "_table" in self.__dir__():
            raise Exception("table not selected")

    def __valid_field(self, field):
        if isinstance(field, str) and field.strip() in self._class.__dict__ and not getattr(self._class, field.strip()).__class__.__name__ in relational_types:
            return field.strip()
        if isinstance(field, list) and field[0] in self._class.__dict__ and not getattr(self._class, field[0]).__class__.__name__ in relational_types:
            return field
        if isinstance(field, str) and "." in field:
            if field.split(".")[0].strip() == self._table and field.split(".")[1].strip() == "*":
                return field.strip()
            if field.split(".")[0].strip() == self._table and field.split(".")[1].strip() in self._class.__dict__ and not getattr(self._class, field.split(".")[1].strip()).__class__.__name__ in relational_types:
                return field.strip()
            if field.split(".")[0].strip() in self._class.__dict__ and getattr(self._class, field.split(".")[0].strip()).__class__.__name__ in relational_types:
                return field.strip()
        raise Exception("{} field does not exist in table".format(field))

    def __valid_relational_table(self, table):
        try:
            if getattr(self._class, table).__class__.__name__ in relational_types:
                return table
            raise Exception("{} table does not exist in relational list".format(table))
        except Exception as e:
            raise Exception("{} table does not exist in relational list".format(table))

    # VALIDAÇÃO DE CAMPOS
    def __check_fields(self, *fields, check_operator=False):
        self.__valid_table()
        list_fields = []
        for field in fields:
            if len(re.findall(r"(([a-z]|[A-Z]|[0-9]|\'|\*){1},{1}\ )", field))>0:
                for item_field in field.split(","):
                    if check_operator:
                        item_field = self.__operator_check(item_field)
                    list_fields.append(self.__valid_field(item_field))
            else:
                if check_operator:
                    field = self.__operator_check(field)
                list_fields.append(self.__valid_field(field))
        return list_fields

    def __check_tables(self, *tables):
        self.__valid_table()
        list_tables = []
        for table in tables:
            if len(re.findall(r"(([a-z]|[A-Z]|[0-9]|\'|\*){1},{1}\ )", table))>0:
                for item_table in table.split(","):
                    list_tables.append(self.__valid_relational_table(item_table))
            else:
                list_tables.append(self.__valid_relational_table(table))
        return list_tables


    def select(self, *fields):
        try:
            self._select = self.__check_fields(*fields)
            return self
        except Exception as e:
            raise e

    def where(self, *fields):
        try:
            self._where = self.__check_fields(*fields, check_operator=True)
            return self
        except Exception as e:
            raise e

    def orwhere(self, *fields):
        try:
            if not self._where  or len(self._where) == 0:
                raise Exception("To use ORWHERE required use before WHERE clause")
            self._orwhere = self.__check_fields(*fields, check_operator=True)
            return self
        except Exception as e:
            raise e

    def having(self, *fields):
        try:
            self._having = self.__check_fields(*fields, check_operator=True)
            return self
        except Exception as e:
            raise e

    def orhaving(self, *fields):
        try:
            if not self._having  or len(self._having) == 0:
                raise Exception("To use ORHAVING required use before HAVING clause")
            self._orhaving = self.__check_fields(*fields, check_operator=True)
            return self
        except Exception as e:
            raise e

    def orderby(self, *fields):
        try:
            self._orderby =  [order if isinstance(order, list) else [order," ", "ASC"] for order in self.__check_fields(*fields, check_operator=True)]
            return self
        except Exception as e:
            raise e

    def groupby(self, *fields):
        try:
            self._groupby = self.__check_fields(*fields, check_operator=True)
            return self
        except Exception as e:
            raise e

    def limit(self, start, end):
        try:
            self._limit = (start, end)
            return self
        except Exception as e:
            raise e

    def join(self, *tables):
        self._join = self.__check_tables(*tables)
        return self

    def include(self, *tables):
        self._include = self.__check_tables(*tables)
        return self

    def _write_select_query(self):
        self.__valid_table()

        # FORMATA SELECT QUERY
        _SELECT = "{}.*".format(self._table) if not self._select and len(self._select) == 0 else ", ".join(["{}.{}".format(self._table, _selected) if "." not in _selected else _selected if _selected.split(".")[0] == self._table else "{0} AS '{0}'".format(_selected) for _selected in list(set().union(self._class.__primary_key__, self._select)) if not "." in _selected or _selected.split(".")[0] == self._table or _selected.split(".")[1] != "*"])
        _SELECTED_FIELDS_JOINS = [_selected for _selected in self._select if _selected.split(".")[0] != self._table and _selected.split(".")[1] == "*" ]
        _FROM = self._table

        if self._join and len(self._join) > 0:
            if not self._select or len(self._select) == 0 or len(_SELECTED_FIELDS_JOINS)>0:
                _SELECT = "{}, {}".format(_SELECT, ",".join([", ".join(["{0}.{1} AS '{0}.{1}'".format(join, field) for field in getattr(self._class, join).type.__dict__ if not field.startswith("_")]) for join in self._join if not self._select or len(self._select) == 0 or "%s.*"%join in _SELECTED_FIELDS_JOINS])).strip()
            if _SELECT.endswith(","):
                _SELECT = _SELECT[:-1]
            _INNER_JOIN = ["INNER JOIN {0} AS {0} ON {0}.{1} = {2}.{3}".format(join, getattr(self._class, join).key, self._table, getattr(self._class, join).reference) for join in self._join]
            _FROM = "{} {}".format(_FROM, "".join(_INNER_JOIN))

        if self._include and len(self._include) > 0:
            if not self._select or len(self._select) == 0 or len(_SELECTED_FIELDS_JOINS)>0:
                _SELECT = "{}, {}".format(_SELECT, ",".join([", ".join(["{0}.{1} AS '{0}.{1}'".format(include, field) for field in getattr(self._class, include).type.__dict__ if not field.startswith("_")]) for include in self._include if not self._select or len(self._select) == 0 or "%s.*"%include in _SELECTED_FIELDS_JOINS])).strip()
            if _SELECT.endswith(","):
                _SELECT = _SELECT[:-1]
            _LEFT_JOIN = ["LEFT JOIN {0} AS {0} ON {0}.{1} = {2}.{3}".format(include, getattr(self._class, include).key, self._table, getattr(self._class, include).reference) for include in self._include]
            _FROM = "{} {}".format(_FROM, "".join(_LEFT_JOIN))

        _QUERY = "SELECT {} FROM {}".format(_SELECT, _FROM)

        if self._where and len(self._where) > 0:
            _WHERE = " AND ".join(["".join(condition) for condition in self._where])
            _QUERY = "{} WHERE ({})".format(_QUERY, _WHERE)
        if self._orwhere and len(self._orwhere) > 0:
            _ORWHERE = " AND ".join(["".join(condition) for condition in self._orwhere])
            _QUERY = "{} OR ({})".format(_QUERY, _ORWHERE)
        if self._groupby and len(self._groupby) > 0:
            _GROUPBY = " ".join(self._groupby)
            _QUERY = "{} GROUP BY {}".format(_QUERY, _GROUPBY)
        if self._having and len(self._having) > 0:
            _HAVING = " AND ".join(["".join(condition) for condition in self._having])
            _QUERY = "{} HAVING ({})".format(_QUERY, _HAVING)
        if self._orhaving and len(self._orhaving) > 0:
            _ORHAVING = " AND ".join(["".join(condition) for condition in self._orhaving])
            _QUERY = "{} OR ({})".format(_QUERY, _ORHAVING)
        if self._orderby and len(self._orderby) > 0:
            _ORDERBY = ", ".join(["".join(condition) for condition in self._orderby])
            _QUERY = "{} ORDER BY {}".format(_QUERY, _ORDERBY)
        if self._limit:
            _QUERY = "{} LIMIT {},{}".format(_QUERY, self._limit[0], self._limit[1])

        return _QUERY

    # EXECUÇÃO DE COMANDO
    def compare(self, obj, reg):
        exists = [getattr(obj, key) == reg[key] for key in self._class.__primary_key__]
        return all(exists)


    @property
    def all(self):
        registros = self._db.fetchall(self._write_select_query())
        object_list = ListType(self._class)
        for linha in registros:
            object_exit = [obj for obj in object_list if self.compare(obj, linha)]
            if len(object_exit)==0:
                obj = self._class(status=2, **linha)
                obj.__status__ = EntityStatus(2)
                object_list.append(obj)
            else :
                object_exit[0].__setrelattr__(**linha)
                object_exit[0].__status__ = EntityStatus(2)

        return object_list

    # EXECUÇÃO DE COMANDO
    @property
    def fetch(self):
        return self._db.fetchall(self._write_select_query())
