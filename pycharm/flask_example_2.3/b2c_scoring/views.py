from b2b_scoring.db import (
    SQL_GET_DATA_FOR_OUTLIER,
    engine
)
import pandas as pd

from flask import jsonify

model = None


def score_common_client():

    raise NotImplementedError


def score_outlier_client(id):
    sql = SQL_GET_DATA_FOR_OUTLIER.substitute(id=id)
    data = pd.read_sql(sql, engine)
    score = model.score(data)
    return jsonify({"score": score})

