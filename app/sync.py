import subprocess

from flask import request, jsonify

from app.main import app


@app.post("/warehouse/sync")
def warehouse_sync():
    """Push the latest warehouse mirror snapshot for a SKU prefix."""
    prefix = request.args.get("prefix", "all")
    result = subprocess.run(
        f"rsync -az /srv/warehouse/{prefix}/ /backups/warehouse/",
        shell=True,
        capture_output=True,
        text=True,
    )
    return jsonify({"rc": result.returncode, "stderr": result.stderr[-500:]})
