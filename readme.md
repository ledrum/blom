# Blóm / stjarna (blom)

**Íslenska** | [English](#english)

Regnbogalituð stjarna eða blóm sem skjaldbaka teiknar með einföldum reglum: **teikna línu, beygja um X gráður, skipta um lit, endurtaka**. Breyttu einni tölu (beygjunni) og þú færð allt aðra mynd.

Ég bjó til svona stjörnur í Logo í tölvutíma í Holtaskóla þegar ég var 16 ára. Ég fékk 10 í tölvu! :P Þetta er sama hugmynd, skrifuð aftur í Python og svo í JavaScript fyrir vefinn.

## Logo-útgáfan

```logo
REPEAT 10000 [SETPC REPCOUNT FD 200 RT :X]
```

Ein lína sem segir: endurtaktu 10.000 sinnum: sett lit eftir númeri umferðarinnar, farðu 200 áfram, beygðu til hægri um X gráður.

## Python-útgáfan (`blom.py`)

Sama hugmynd með tveimur breytingum: línan **styttist um eitt skref í hverri umferð** (frá 300 niður í 0), og litirnir koma úr lista sem er endurtekinn:

```python
while LENGD > 0:
    s.pencolor(LITIR[skref % len(LITIR)])
    s.forward(LENGD)
    s.right(X)
    skref = skref + 1
    LENGD = LENGD - 1
```

Prófaðu að breyta `X` efst í skránni. Nokkrar tölur sem gefa fallegar myndir: `170`, `144`, `160`, `175`, `91`, `121`, `119`, `95`. Talan `144` gefur klassíska fimmarma stjörnu.

### Keyra

```bash
python3 blom.py
```

Þarf `turtle`, sem fylgir með Python (það notar `tkinter`). Lokaðu glugganum til að hætta.

## Vefútgáfan (`vefur/blom-blokk.html`)

Sama teikning í JavaScript með `<canvas>`. Þar er hægt að breyta beygjunni og upphafslengdinni og horfa á stjörnuna teiknast. Skráin er skrifuð sem **Custom HTML blokk fyrir WordPress**: opnaðu hana, afritaðu allt og límdu í Custom HTML blokk. Hún þarf engin gögn af þjóninum og er á íslensku og ensku.

JavaScript-útgáfan var skrifuð með hjálp Claude (Anthropic) þegar ég var að læra að þýða Python yfir í JavaScript. Python-útgáfan er mín.

## Hvernig virkar þetta?

Þetta er *skjaldbökuteikning* (turtle graphics) eins og í Logo. Skjaldbakan hefur stöðu og stefnu, og tvær skipanir duga: áfram (`forward`) og beygja (`right`). Í vefútgáfunni reiknar kóðinn stöðuna sjálfur með sínus og kósínus, safnar saman öllum punktunum, finnur stærð myndarinnar og stækkar eða minnkar hana til að passa í rammann.

## Leyfi

MIT, sjá `LICENSE`.

---

<a id="english"></a>

# Flower / star (blom, English)

A rainbow-coloured star or flower drawn by a turtle with simple rules: **draw a line, turn X degrees, change colour, repeat**. Change one number (the turn angle) and you get a completely different picture.

I made stars like this in Logo in a computer class at Holtaskóli when I was 16. I got a 10 in computing! :P This is the same idea, rewritten in Python and then in JavaScript for the web.

## The Logo version

```logo
REPEAT 10000 [SETPC REPCOUNT FD 200 RT :X]
```

One line that says: repeat 10,000 times: set the pen colour from the repeat number, move forward 200, turn right X degrees.

## The Python version (`blom.py`)

The same idea with two changes: the line gets **one step shorter every round** (from 300 down to 0), and the colours come from a list that is cycled:

```python
while LENGD > 0:
    s.pencolor(LITIR[skref % len(LITIR)])
    s.forward(LENGD)
    s.right(X)
    skref = skref + 1
    LENGD = LENGD - 1
```

Try changing `X` at the top of the file. Some angles that give nice pictures: `170`, `144`, `160`, `175`, `91`, `121`, `119`, `95`. The value `144` gives the classic five-pointed star.

### Run

```bash
python3 blom.py
```

Needs `turtle`, which ships with Python (it uses `tkinter`). Close the window to quit.

## The web version (`vefur/blom-blokk.html`)

The same drawing in JavaScript using `<canvas>`. You can change the turn angle and the starting length and watch the star being drawn. The file is written as a **WordPress Custom HTML block**: open it, copy everything and paste it into a Custom HTML block. It needs no server-side data and comes in Icelandic and English.

The JavaScript version was written with help from Claude (Anthropic) while I was learning to translate Python into JavaScript. The Python version is my own.

## How does it work?

This is *turtle graphics*, as in Logo. The turtle has a position and a heading, and two commands are enough: forward and right. In the web version the code computes the position itself with sine and cosine, collects all the points, finds the size of the picture and scales it to fit the frame.

## License

MIT, see `LICENSE`.