from .db import (
    SQL_GET_DATA_FOR_OUTLIER,
    engine
)

from flask import (
    jsonify,
    Blueprint
)

import pandas as pd

bp_b2b = Blueprint(name='b2b_blueprint',
               import_name=__name__,
               url_prefix='/b2b/')

model = None


@bp_b2b.route("/score/common")
def score_common_client():
    raise NotImplementedError


@bp_b2b.route("/score/outlier")
def score_outlier_client(id):
    sql = SQL_GET_DATA_FOR_OUTLIER.substitute(id=id)
    data = pd.read_sql(sql, engine)
    score = model.score(data)
    return jsonify({"score": score})

