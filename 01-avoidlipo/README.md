# 50,000 Woofs

## Nov. 1: *#avoidlipo* -- Your text may not contain any "e"s

We all know a word containing "e"s.

> *meow*

And we all know a word not containing "e"s.

> *woof*

Here is my entry for [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014/),
[*50,000 Meows*](https://github.com/hugovk/meow.py) refactored (copied and pasted) into
[*50,000 Woofs*](https://github.com/hugovk/meow.py) (including unit tests).

### Usage

```bash
cp ../data/pg2701.txt .
python3 woof.py pg2701.txt > woof-pg2701.txt
python3 woof.py --translation pg2701.txt > woof-x2-pg2701.txt

# Or with PDFs, needs py2pdf.py and 'pip install reportlab'
./woof.sh pg2701.txt "Moby Dick; or Th Whal, by Hrman Mlvill"
```

### Output

| Original                                                                     |                        woof                        |  words |                     with translation                    |  words |
|------------------------------------------------------------------------------|:--------------------------------------------------:|:------:|:-------------------------------------------------------:|:------:|
| [*Moby Dick; or The Whale*, by Herman Melville](../data/pg2701.txt?raw=true)                   |  [txt](woof-pg2701.txt?raw=true) [pdf]( woof-pg2701.pdf?raw=true)  | 215,136 |  [txt](woof-x2-pg2701.txt?raw=true) [pdf](woof-x2-pg2701.pdf?raw=true)  | 430,272 |

### Extracts

Here's part of *Moby Dick; or Th Whal, by Hrman Mlvill*:
```
"WOOOF.... Wf. wof Wof. WOOF. Woof woooof wf wooof woof wooooooof wf
wooooof; wof wf Wof. WOOOF wf woooof wf wooooof." --WOOOOOF'W WOOOOOOOOF

"WOOOF.... Wf wf woof wooooooooof woof wof Wof. wof Wof. WOOOOF; W.W.
WOOF-WOF, wf woof, wf woooof." --WOOOOOOOOF'W WOOOOOOOOF

     WOOOF,               WOOOF.
     WOOOF,               WOOOF.
     WOOOF,               WOOOF-WOOOF.
     WOOOF,               WOOOOF.
     WOF,                 WOOOF.
     WOOF,                WOOOOOF.
     WOOOF,               WOOOOOOOF.
     WOOOF,               WOOOOOF.
     WOOOOOF,             WOOOOF.
     WOOOOOF,             WOOOOOF.
     WOOOF-WOOF-WOOF,     WOOOF.
     WOOOF-WOOF-WOOF,     WOOOOOOOOOF.

WOOOOOOF (Woooooof wf w Wof-Wof-Wooooooof).
```

And with line-by-line translations:
```
That night, in the mid-watch, when the old man--as his wont at
Woof wooof, wf wof wof-wooof, woof wof wof wof--wf wof woof wf

intervals--stepped forth from the scuttle in which he leaned, and went
wooooooof--wooooof wooof woof wof wooooof wf wooof wf woooof, wof woof

to his pivot-hole, he suddenly thrust out his face fiercely, snuffing
wf wof wooof-woof, wf woooooof woooof wof wof woof woooooof, woooooof

up the sea air as a sagacious ship's dog will, in drawing nigh to
wf wof wof wof wf w wooooooof woof'w wof woof, wf wooooof woof wf

some barbarous isle. He declared that a whale must be near. Soon that
woof wooooooof woof. Wf woooooof woof w wooof woof wf woof. Woof woof

peculiar odor, sometimes to a great distance given forth by the
woooooof woof, wooooooof wf w wooof woooooof wooof wooof wf wof

living sperm whale, was palpable to all the watch; nor was any mariner
woooof wooof wooof, wof woooooof wf wof wof wooof; wof wof wof wooooof

surprised when, after inspecting the compass, and then the dog-vane, and
wooooooof woof, wooof woooooooof wof wooooof, wof woof wof wof-woof, wof

then ascertaining the precise bearing of the odor as nearly as possible,
woof woooooooooof wof wooooof wooooof wf wof woof wf woooof wf woooooof,

Ahab rapidly ordered the ship's course to be slightly altered, and the
Woof wooooof wooooof wof woof'w woooof wf wf woooooof wooooof, wof wof

sail to be shortened.
woof wf wf wooooooof.
```
