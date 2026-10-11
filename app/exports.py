import os

from flask import request, send_file

from app.main import app

EXPORT_ROOT = "/srv/exports"


@app.get("/exports/<name>")
def download_export(name):
    """Download one of the nightly inventory export files."""
    path = os.path.join(EXPORT_ROOT, name)
    return send_file(path)
