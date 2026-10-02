## Layers (no combos)

![Layers](visualization/chocofi-keys.svg)

## Layers with combos

![Layers with combos](visualization/chocofi.svg)

## NAV shortcuts (both keyboards)

Tap NAV once, then one of these keys; no separate Ctrl press is needed:

| Key | Action |
| --- | --- |
| M | Previous desktop (`Ctrl+Left`) |
| , | Next desktop (`Ctrl+Right`) |
| N | Mission Control (`Ctrl+Up`) |
| F / G | Existing back/forward shortcuts (`Cmd+[` / `Cmd+]`), moved from M / , |

## Go60

`config/go60.keymap` is a Go60 port of the Chocofi layout with a compact hybrid
footprint. It keeps the number row, the left outer `Tab`, `Esc`, and MoErgo
keys, the right home-row apostrophe/right bottom-row Backspace positions, and
six Chocofi thumb functions. Each hand uses the two nearer angled keys (T1/T2)
and the straight R5C2 key immediately beside T1. This preserves the physical
Chocofi grouping:

| Go60 position | Left hand | Right hand |
| --- | --- | --- |
| R5C2 (straight key beside T1, under V/M) | NUM | NAV |
| T1 (nearest B/N; default right Enter) | SYM | Space |
| T2 | Shift | Ctrl |
| T3 (farthest angled key) | Inactive | Inactive |

The remaining straight lower keys and right outer finger column are inactive
on Base. The QWERTY, NUM, SYM, NAV, and SET layers, Mac modifiers, and Chocofi
combos are retained. On NUM, right T2 taps `0` and holds Ctrl; on SYM/NAV/SET
it is sticky Ctrl. Right T1 returns to Base on all four of those layers.
NUM, SYM, Shift, and NAV remain on their corresponding physical positions.

The physical MoErgo key taps status indicators and holds the Magic layer with
RGB, Bluetooth, USB, media, and reset controls. `NAV + N` sends Ctrl+Up for
macOS Exposé/Mission Control. The integrated right touchpad remains mouse
input; the left touchpad scrolls and its click acts as right-click. Normal
scrolling uses a gentle 1/16 scale; with NAV active it uses 1/8 (twice as fast).
Both horizontal and vertical scrolling are scaled, and vertical scrolling
keeps the Mac-style natural direction. SET retains its left-pad mouse mode.

The Go60 workflow builds the left and right halves into one `go60.uf2`
artifact using the official MoErgo ZMK distribution. Push the repository and
download that artifact from the **Build Go60 firmware** GitHub Actions run.
