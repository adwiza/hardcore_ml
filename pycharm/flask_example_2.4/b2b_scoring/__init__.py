from . import db


def init_postgres(host: str, port: int):
    if db.engine is None:
        # Еще не создан - создайте
        db.engine = ...  # Создание подключения
    else:
        # Коннект уже почему то создан
        pass


def init_model():
    pass