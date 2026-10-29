#!/usr/bin/env python3
"""Export the SSP controls workbook to a diff-friendly CSV.

Usage:
    python scripts/export_controls.py
    python scripts/export_controls.py path/to/workbook.xlsx path/to/out.csv

Requires: openpyxl (pip install openpyxl)
"""
import csv
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_IN = ROOT / "deliverables/05-system-security-plan/SSP_Controls_Selection_Team_5.xlsx"
DEFAULT_OUT = ROOT / "data/ssp_controls_selection.csv"

COLUMNS = [
    "control_id",
    "control_name",
    "family",
    "implementation_description",
    "control_type",
    "implementation_level",
    "moderate_baseline",
    "ot_overlay",
    "tailored_or_inherited",
    "modified_for_ssp",
]


def flag(value) -> str:
    return "yes" if value is not None and str(value).strip() else "no"


def main(src: Path, dst: Path) -> None:
    ws = openpyxl.load_workbook(src, data_only=True).worksheets[0]
    rows = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if not r[1]:
            continue
        (_sort, cid, name, desc, ctype, impl, moderate, ot, ti, modified) = r[:10]
        rows.append({
            "control_id": cid.strip(),
            "control_name": (name or "").strip(),
            "family": cid.split("-")[0],
            "implementation_description": " ".join((desc or "").split()),
            "control_type": (ctype or "").strip(),
            "implementation_level": (impl or "").strip(),
            "moderate_baseline": flag(moderate),
            "ot_overlay": flag(ot),
            "tailored_or_inherited": (ti or "").strip(),
            "modified_for_ssp": flag(modified),
        })
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} controls to {dst.relative_to(ROOT) if dst.is_relative_to(ROOT) else dst}")


if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_IN
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    main(src, dst)
