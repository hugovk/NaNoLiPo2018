# 50,000 ~Woofs~ Moos

## Or Mooby Dick; Or the White Sea Cow

## Nov. 6: **#mirrorlipo** -- You may only use letters that have at least one axis of symmetry.


We all know a word whose letters all have at least one axis of symmetry.

> *woof*

F it. Let's try another.

> *moo*

Here is my entry for [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014/),
[*50,000 Meows*](https://github.com/hugovk/meow.py) refactored (copied and pasted) into
[*50,000 Woofs*](https://github.com/hugovk/NaNoLiPo2018/tree/master/01-avoidlipo) 
(including unit tests), refactored (copied and pasted) into *50,000 Moos*.

### Usage

```bash
cp ../data/pg2701.txt .
python3 moo.py pg2701.txt > moo-pg2701.txt
python3 moo.py --translation pg2701.txt > moo-x2-pg2701.txt

# Or with PDFs, needs py2pdf.py and 'pip install reportlab'
./moo.sh pg2701.txt "Mo Dick; o T Wal, Hman Mlvill (or Mooby Dick; Or the White Sea Cow)"
```

### Output

| Original                                                                     |                        meow                        |  words |                     with translation                    |  words |
|------------------------------------------------------------------------------|:--------------------------------------------------:|:------:|:-------------------------------------------------------:|:------:|
| [*Moby Dick; or The Whale*, by Herman Melville](../data/pg2701.txt?raw=true)                   |  [txt](moo-pg2701.txt?raw=true) [pdf]( moo-pg2701.pdf?raw=true)  | 215,136 |  [txt](moo-x2-pg2701.txt?raw=true) [pdf](moo-x2-pg2701.pdf?raw=true)  | 430,272 |

### Extracts

Here's part of *Mo Dick; o T Wal, Hman Mlvill (or Mooby Dick; Or the White Sea Cow)*:
```
"MOOOO.... Mo. moo Moo. MOOO. Mooo mooooo mo moooo mooo moooooooo mo
moooooo; moo mo Moo. MOOOO mo mooooo mo moooooo." --MOOOOOO'M MOOOOOOOOO

"MOOOO.... Mo mo mooo moooooooooo mooo moo Moo. moo Moo. MOOOOO; M.M.
MOOO-MOO, mo mooo, mo mooooo." --MOOOOOOOOO'M MOOOOOOOOO

     MOOOO,               MOOOO.
     MOOOO,               MOOOO.
     MOOOO,               MOOOO-MOOOO.
     MOOOO,               MOOOOO.
     MOO,                 MOOOO.
     MOOO,                MOOOOOO.
     MOOOO,               MOOOOOOOO.
     MOOOO,               MOOOOOO.
     MOOOOOO,             MOOOOO.
     MOOOOOO,             MOOOOOO.
     MOOOO-MOOO-MOOO,     MOOOO.
     MOOOO-MOOO-MOOO,     MOOOOOOOOOO.

MOOOOOOO (Mooooooo mo m Moo-Moo-Moooooooo).
```

And with line-by-line translations:
```
Fishiest of all fishy places was the Try Pots, which well deserved
Mooooooo mo moo moooo mooooo moo moo Moo Mooo, moooo mooo mooooooo

its name; for the pots there were always boiling chowders. Chowder for
moo mooo; moo moo mooo moooo mooo mooooo moooooo mooooooo. Moooooo moo

breakfast, and chowder for dinner, and chowder for supper, till you
moooooooo, moo moooooo moo mooooo, moo moooooo moo mooooo, mooo moo

began to look for fish-bones coming through your clothes. The area
moooo mo mooo moo mooo-moooo mooooo moooooo mooo moooooo. Moo mooo

before the house was paved with clam-shells. Mrs. Hussey wore a polished
mooooo moo moooo moo moooo mooo mooo-mooooo. Moo. Mooooo mooo m mooooooo

necklace of codfish vertebra; and Hosea Hussey had his account books
mooooooo mo moooooo mooooooo; moo Moooo Mooooo moo moo moooooo moooo

bound in superior old shark-skin. There was a fishy flavor to the milk,
moooo mo mooooooo moo moooo-mooo. Moooo moo m moooo mooooo mo moo mooo,

too, which I could not at all account for, till one morning happening
moo, moooo M moooo moo mo moo moooooo moo, mooo moo moooooo moooooooo

to take a stroll along the beach among some fishermen's boats, I saw
mo mooo m mooooo moooo moo moooo moooo mooo moooooooo'm moooo, M moo

Hosea's brindled cow feeding on fish remnants, and marching along the
Moooo'm mooooooo moo moooooo mo mooo mooooooo, moo mooooooo moooo moo

sand with each foot in a cod's decapitated head, looking very slip-shod,
mooo mooo mooo mooo mo m moo'm moooooooooo mooo, moooooo mooo mooo-mooo,

I assure ye.
M mooooo mo.
```
