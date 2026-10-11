from flask import request, jsonify

from app.main import ITEMS, app


@app.post("/reports/adhoc")
def adhoc_report():
    """Evaluate a filter expression written in the dashboard's query box."""
    expr = request.form.get("expr", "True")
    rows = list(ITEMS.values())
    result = [r for r in rows if eval(expr, {"r": r})]
    return jsonify(result)
