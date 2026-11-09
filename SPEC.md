# ankiSOL — specification (draft 0.1)

*a Galactic Administrative System (GAS) named after Sumerian & Norse mythologies*

Status: **draft**. Sections marked **OPEN** are undecided.

---

## 1. Purpose

ankiSOL is a way to divide any habitable sphere into the same **108 harmonies**, grouped into **9 melodies**. Every planet and moon gets the identical grid, so a place on one world has a matching place on every other.

The aim is to spread a civilization's interest in its neighboring worlds across all of its people, the way "sister cities" work, without armed conflict or expensive financial machinery. No single interest can claim a whole world, because every world is divided the same way and every stewardship archetype (§7) holds ground on it.

108 is meant to be small enough for anyone on a planet to learn a few facts about each harmony, and so to care about being represented through them.

## 2. Name and glyphs

**𒀭𒆠☉** — read *anki sol*.

- **𒀭 An** — the Sumerian sky / heaven. The same cuneiform sign is the *dingir* determinative that marks divinity.
- **𒆠 Ki** — the Sumerian earth.
- **𒀭𒆠 Anki** — "heaven-and-earth", the Sumerian word for the universe as a whole. The pairing echoes other first couples, such as Ask & Embla, and **Æ**.
- **☉ Sól** — the Norse sun (runic: **ᛊᛟᛚ**). The circled point can be read as a sun and its orbit, a city and its wall, a garden and its fence, a navel, Midgard, or a targeting reticle. The ambiguity is intended.

### 2.1 Reading (mythopoetic intent)

*This section is interpretation, not definition. The glyph notes above are the factual layer; this is what the name is meant to carry.*

An is the absent sky-father, philandering among the stars. Ki is the mother who stays with her young: the living earth that pigments our skin. To a child looking up from the crib, An's universe seems dead, but it hangs full of enchanting curiosities, like a mobile turning above. ankiSOL can be read as the mother's explanation of the roaming father to their children. Perhaps a cultivating *Homo sapiens* explaining her wandering Neanderthal mate.

The system mirrors that pairing. The grid is An's work: cold geometry pinned the same way onto every sphere. The archetypes are Ki's work: stewardship of living ground. Together they bring the sky's endless worlds home and divide them among the children, so no single child inherits everything.

So the naming is meant to put a mythopoetic intention into the systematics. It offers the modern scientist a useful model that shines, while reminding them that systematic knowledge grew out of the speculative realm alchemy was born in. The certainty of the shine rests on the strange shades of what could be, and every new hypothesis sprouts from that compost.

## 3. Vocabulary

| term | meaning |
|---|---|
| **anki** | the whole system of systems |
| **star** | a system's primary, e.g. ☉ Sol |
| **song** | a body orbiting a star (planet, dwarf planet, …) |
| **movement** | a body orbiting a song (a moon) |
| **melody** | one of 9 large tiles of a song or movement |
| **harmony** | one of 108 cells of a song or movement (12 per melody) |

Example: Earth is *Sol's 3rd song*. Luna is *the 1st movement of Sol's 3rd song*.

## 4. Address format

```
𒀭𒆠 . ☉ . SSS . MMM . Hh
anki  star song movement harmony
```

- **SSS** — song number, 3 digits.
- **MMM** — movement number, 3 digits. `000` is the song itself.
- **Hh** — harmony: column letter `a`–`l` + row digit `1`–`9`.

Every address has the same number of fields. Add more digits only when there is a real need, e.g. a 1000th song worth caring about.

| place | glyph form | ASCII form |
|---|---|---|
| Earth, harmony b3 | `𒀭𒆠.☉.003.000.b3` | `anki.sol.003.000.b3` |
| Luna, harmony b3 | `𒀭𒆠.☉.003.001.b3` | `anki.sol.003.001.b3` |
| Mars, harmony b3 | `𒀭𒆠.☉.004.000.b3` | `anki.sol.004.000.b3` |

Data storage should use the plain code (`b3`, melody `7`). Glyph names (§6.4) are for emotional expression and longer-form writing.

Finer detail — nearest city, the country or empire currently claiming the land, the era — sits *below* the harmony. It is expected to change over time and is not part of the address.

**OPEN:** the glyph or ASCII token for stars other than Sol.

## 5. Numbering rules

### 5.1 Songs — by distance

Songs are numbered outward from their star (Earth = `003`, Mars = `004`).

Song numbers are **not permanent**. A newly found inner body, or a reclassification, shifts the numbers outward. Bodies in unusual orbits (e.g. a song that loops in a figure-8 around two stars) are numbered by convention at the time and noted as exceptions.

### 5.2 Movements — by discovery

Movements are numbered in **order of discovery**. Ties within the same year are broken by announcement date, then by catalog designation. This follows existing astronomical practice (Titan is Saturn VI).

Movement numbers are **permanent**. A new discovery never changes an existing address.

## 6. Grid geometry

The grid is purely angular, so it fits any sphere regardless of its size or surface.

### 6.1 Harmonies

- **Columns `a`–`l`**: 12 columns of 30° longitude each. Column `a` starts at the body's *west edge* meridian (§6.3).
- **Rows `1`–`9`**: 9 rows of 20° latitude each. Row 1 runs from the north pole to 70°N. Row lines fall at ±70°, ±50°, ±30° and ±10°.
- Edges follow the **parallels and meridians exactly**, not great-circle approximations.

### 6.2 Melodies

The 9 melodies follow a rule-of-thirds map: 3 longitude thirds (120° each) × 3 latitude bands (pole–30°, 30°N–30°S, 30°–pole).

| melody | columns | rows | Earth bounds |
|---|---|---|---|
| 1 first | i–l | 1–3 | North Pole – 30°N, 75°E – 165°W |
| 2 second | i–l | 4–6 | 30°N – 30°S, 75°E – 165°W |
| 3 third | i–l | 7–9 | 30°S – South Pole, 75°E – 165°W |
| 4 fourth | e–h | 1–3 | North Pole – 30°N, 45°W – 75°E |
| 5 fifth | e–h | 4–6 | 30°N – 30°S, 45°W – 75°E |
| 6 sixth | e–h | 7–9 | 30°S – South Pole, 45°W – 75°E |
| 7 seventh | a–d | 1–3 | North Pole – 30°N, 165°W – 45°W |
| 8 eighth | a–d | 4–6 | 30°N – 30°S, 165°W – 45°W |
| 9 ninth | a–d | 7–9 | 30°S – South Pole, 165°W – 45°W |

**Reading directions are deliberately mixed:**

- **Melodies** count in *manga* direction: right to left, top to bottom.
- **Harmonies** count in *comic* direction: left to right, top to bottom.

So depending on point of view, any group of representatives sorts to the top, the bottom, or the middle by default. This is settled at the design stage on purpose, before anyone holds a seat to defend.

### 6.3 Per-body reference conventions

Each song or movement needs a defined:

1. **Zero longitude** — the body's own prime meridian (Earth: Greenwich; Mars: the Airy-0 crater; Luna: the mean Earth-facing direction).
2. **West edge** — where column `a` starts, relative to zero longitude. **Earth: 165°W.** The 15° offset from Greenwich is a deliberate compromise with historical precedent, in the same spirit as the Holocene calendar adding 10,000 years.
3. **North** — by the IAU right-hand rule (the north pole is the one around which the body spins counter-clockwise). This keeps the first melody consistent on bodies that rotate backwards or are tipped over. Magnetic poles do not count; they wander and have flipped before.

**OPEN:** default west-edge offsets for Luna, Mars and others. Inherit 165° west of their zero? Or justify a local offset from a first habitat or natural feature?

### 6.4 Harmony glyph names

Each column letter has a long-form name that mixes scripts on purpose. The point is to keep many glyph traditions in the cartography rather than defaulting to Latin.

| col | long form |
|---|---|
| a | alpha |
| b | βῆτα |
| c | cee |
| d | delta |
| e | **OPEN** |
| f | **OPEN** |
| g | **OPEN** |
| h | **OPEN** |
| i | ιώτα |
| j | ʥえ (jay) |
| k | κάππα |
| l | lambda |

Long form: `<column-name>·<row>`. E.g. `βῆτα·3` = b3, read *beta three*.

### 6.5 Areas (Earth, WGS84)

Melody areas, with edges on true parallels:

| melodies | area |
|---|---|
| 1, 3, 4, 6, 7, 9 (polar) | 42,647,977 km² each |
| 2, 5, 8 (middle) | 84,725,920 km² each |
| total | 510,065,622 km² |

Harmonies and melodies are intentionally **unequal** in area. Species are not equal in size within a set or across sets either. A melody does not need to be long to hold its emotional space in a composition.

## 7. Stewardship archetypes

Twelve archetypes share stewardship of each world:

> bard · sorcerer · druid · fighter · ranger · barbarian · paladin · cleric · monk · rogue · wizard · warlock

Proposed rule (**OPEN**): **each melody holds all 12 archetypes exactly once.** Then:

- every archetype holds **9 harmonies on every song and movement**, one per melody;
- every archetype has ground in the north, the middle band and the south, so its people, animals and plants can move as the climate changes;
- no archetype can claim a whole world against the others.

Each archetype names a **capital harmony** on each body. A capital may be unconventional, such as a floating city (monks) or a vagabond city (rangers).

Example assignment — seventh melody of Earth:

| harmony | biome | archetype |
|---|---|---|
| a1 | oceans | bard |
| b1 | islands | sorcerer |
| c1 | islands | druid |
| d1 | polar desert | fighter |
| a2 | forests | ranger |
| b2 | forests | barbarian |
| c2 | plain | paladin |
| d2 | plain | cleric |
| a3 | oceans | monk |
| b3 | deserts | rogue |
| c3 | plain | wizard |
| d3 | forests | warlock |

Druids are associated with first peoples. Their biomes vary by melody (tundra, tropical forest, …).

Resources, habitats, inhabitants and names all change over time. Assignments describe stewardship, not ownership.

## 8. Open questions

- Glyph and ASCII tokens for stars other than ☉.
- Column long-form names e–h.
- West-edge offsets for bodies other than Earth.
- Whether every melody must hold all 12 archetypes (§7).
- Whether a harmony on a body nobody has visited can carry law, or stays dormant until a settlement exists.
- How assignments are revised when biomes shift.

---

*ankiSOL is a project of smg108f. This specification is licensed under CC BY-SA 4.0 (see LICENSE.md).*
