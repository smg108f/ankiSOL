#!/usr/bin/env python3
"""
ankiSOL — 108-harmony grid generator.  (MIT License, (c) 2026 smg108f)
Spec: ../SPEC.md

Grid (angular, so it fits any sphere):
  columns a–l : 12 × 30° of longitude, column a starting at the WEST_EDGE meridian
  rows    1–9 : 9 × 20° of latitude, row 1 at the north pole
  melodies    : 9 tiles of 4 columns × 3 rows, numbered per the rule-of-thirds map
                (1–3 = columns i–l, 4–6 = e–h, 7–9 = a–d; top to bottom)

Edges are densified along the parallels so viewers that draw straight
great-circle edges (Google Earth) still follow the true latitude lines.

Usage:
  python3 tools/ankisol_grid.py [--body earth] [--west-edge -165] [--out data/earth.kml]
"""
import argparse
from xml.sax.saxutils import escape

COLS = "abcdefghijkl"
STEP = 0.5  # degrees between densified points

# KML colors are aabbggrr; one per melody
MELODY_COLORS = {
    1: "6633a1ff", 2: "66ff9933", 3: "6633cc66",
    4: "66cc33cc", 5: "6600ccff", 6: "66ffcc00",
    7: "663366ff", 8: "6699cc33", 9: "66cc9966",
}


def wrap(lon):
    return ((lon + 180.0) % 360.0) - 180.0


def frange(a, b, step):
    n = max(1, int(round(abs(b - a) / step)))
    return [a + (b - a) * i / n for i in range(n + 1)]


def cell_bounds(col, row, west_edge):
    ci = COLS.index(col)
    west = west_edge + 30 * ci
    east = west + 30
    north = 90 - 20 * (row - 1)
    south = north - 20
    return north, south, west, east


def melody_of(col, row):
    group = COLS.index(col) // 4          # 0 = a–d, 1 = e–h, 2 = i–l
    band = (row - 1) // 3                 # 0 = north, 1 = middle, 2 = south
    return (2 - group) * 3 + band + 1


def ring(north, south, west, east):
    pts = []
    pts += [(lon, north) for lon in frange(west, east, STEP)]          # north edge →
    pts += [(east, lat) for lat in frange(north, south, STEP)][1:]     # east edge ↓
    pts += [(lon, south) for lon in frange(east, west, STEP)][1:]      # south edge ←
    pts += [(west, lat) for lat in frange(south, north, STEP)][1:]     # west edge ↑
    return " ".join(f"{wrap(lon):.6f},{lat:.6f},0" for lon, lat in pts)


def fmt_lon(lon):
    lon = wrap(lon)
    if lon in (180.0, -180.0):
        return "180°"
    return f"{abs(lon):g}°{'E' if lon > 0 else 'W' if lon < 0 else ''}"


def fmt_lat(lat):
    if lat == 90:
        return "North Pole"
    if lat == -90:
        return "South Pole"
    return f"{abs(lat):g}°{'N' if lat > 0 else 'S' if lat < 0 else ''}"


def build(body, west_edge):
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<kml xmlns="http://www.opengis.net/kml/2.2">',
        "<Document>",
        f"<name>ankiSOL harmonies of {escape(body)}</name>",
        f"<description>a proposed 108-harmony segmentation of {escape(body)}. "
        f"columns a–l (30° each, from {fmt_lon(west_edge)}), rows 1–9 (20° each, from the north pole).</description>",
    ]
    for m, color in MELODY_COLORS.items():
        out.append(
            f'<Style id="m{m}"><LineStyle><color>ff{color[2:]}</color><width>1.5</width></LineStyle>'
            f"<PolyStyle><color>{color}</color></PolyStyle></Style>"
        )

    ordinals = ["first", "second", "third", "fourth", "fifth",
                "sixth", "seventh", "eighth", "ninth"]
    for m in range(1, 10):
        cells = [(c, r) for r in range(1, 10) for c in COLS if melody_of(c, r) == m]
        rows = [r for _, r in cells]
        cols = [c for c, _ in cells]
        n, _, w, _ = cell_bounds(cols[0], rows[0], west_edge)
        _, s, _, e = cell_bounds(cols[-1], rows[-1], west_edge)
        out.append("<Folder>")
        out.append(f"<name>{ordinals[m-1]}-melody</name>")
        out.append(
            f"<description>{fmt_lat(n)} to {fmt_lat(s)}, {fmt_lon(w)} to {fmt_lon(e)}</description>"
        )
        for c, r in cells:
            north, south, west, east = cell_bounds(c, r, west_edge)
            code = f"{c}{r}"
            out.append("<Placemark>")
            out.append(f"<name>{code}</name>")
            out.append(
                f"<description>{code} of {escape(body)} · {ordinals[m-1]}-melody · "
                f"{fmt_lat(north)} to {fmt_lat(south)}, {fmt_lon(west)} to {fmt_lon(east)}</description>"
            )
            out.append(f"<styleUrl>#m{m}</styleUrl>")
            out.append("<ExtendedData>"
                       f'<Data name="harmony"><value>{code}</value></Data>'
                       f'<Data name="melody"><value>{m}</value></Data>'
                       f'<Data name="body"><value>{escape(body)}</value></Data>'
                       "</ExtendedData>")
            out.append("<Polygon><tessellate>1</tessellate><outerBoundaryIs><LinearRing>"
                       f"<coordinates>{ring(north, south, west, east)}</coordinates>"
                       "</LinearRing></outerBoundaryIs></Polygon>")
            out.append("</Placemark>")
        out.append("</Folder>")
    out += ["</Document>", "</kml>"]
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--body", default="earth")
    ap.add_argument("--west-edge", type=float, default=-165.0,
                    help="longitude of column a's western edge (earth: -165)")
    ap.add_argument("--out")
    a = ap.parse_args()
    path = a.out or f"{a.body}.kml"
    with open(path, "w", encoding="utf-8") as f:
        f.write(build(a.body, a.west_edge))
    print(path)
