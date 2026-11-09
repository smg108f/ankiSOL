# 𒀭𒆠☉ ankiSOL

**a Galactic Administrative System (GAS) named after Sumerian & Norse mythologies**

ankiSOL divides any habitable sphere into **108 harmonies** in **9 melodies**, using the same grid on every world. Places on Earth, Luna, Mars or Titan pair up the way sister cities do. Stewardship is shared among twelve archetypes, so no single interest can claim a whole world.

```
𒀭𒆠.☉.003.000.b3   →   anki · Sol · 3rd song · (the song itself) · βῆτα·3
```

## Contents

| path | what |
|---|---|
| [`SPEC.md`](SPEC.md) | the specification (draft) |
| [`tools/ankisol_grid.py`](tools/ankisol_grid.py) | generator for the 108-harmony grid as KML, for any body |
| [`data/earth.kml`](data/earth.kml) | Earth's grid — import into Google Earth (File → Import) |

## Generate a grid

```sh
python3 tools/ankisol_grid.py --body earth --out data/earth.kml
python3 tools/ankisol_grid.py --body luna  --west-edge -165 --out data/luna.kml
```

Python 3 only, no dependencies. Edges are densified along the parallels so they follow true latitude lines. On Earth, the nine melodies tile the WGS84 surface exactly (510,065,622 km²).

## Status

Draft 0.1. Open questions are listed in [SPEC.md §8](SPEC.md#8-open-questions).

## License

- Specification and documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- Code (`tools/`): [MIT](https://opensource.org/license/mit)

See [LICENSE.md](LICENSE.md).

---

a project of [smg108f](https://smg108f.ink)
