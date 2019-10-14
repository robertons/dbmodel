
# Python DataBase Entity Model - Python3

SDK fornece uma série de recursos que aumentam muito a produtividade no desenvolvimento de aplicações integrada a banco de dados com gerenciamento de objeto.

# Instalação
Instalação utilizando Pip
```bash
pip install dbmodelpy
```
Git/Clone
```
git clone https://github.com/robertons/dbmodelpy
cd dbmodelpy
pip install -r requirements.txt
python setup.py install
```

## Configuração

```python
import dbmodelpy

dbmodelpy.Make(dir = os.path.dirname(os.path.abspath(__file__)), db_user="user", db_password="pass", db_host="host", db_port=3306, db_database="dbname")

```

## Make Will Generate Model Folder With Entities

.
├── ...
├── model                    # Entity Model Folder (alternatively `spec` or `tests`)
│   ├── __init__.py          
│   ├── table_a              # TableA Entity Class
│   ├── table_b              # TableB Entity Class
│   └── table_b              # TableC Entity Class
└── ...
