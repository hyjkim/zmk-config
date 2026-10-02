## Layers (no combos)

![Layers](visualization/chocofi-keys.svg)

## Layers with combos

![Layers with combos](visualization/chocofi.svg)

## Go60

`config/go60.keymap` is a Go60 port of the Chocofi layout with a compact hybrid
footprint. It keeps the number row, the left outer `Tab`, `Esc`, and MoErgo
keys, the six Chocofi thumb controls, and the right home-row apostrophe/right
bottom-row Backspace positions. The right outer finger column and extra lower
keys remain inert. It keeps the QWERTY, NUM, SYM, NAV, and SET layers, Mac
modifiers, and the Chocofi combos translated to Go60 key positions.

The physical MoErgo key taps status indicators and holds the Magic layer with
RGB, Bluetooth, USB, media, and reset controls. `NAV + N` sends Ctrl+Up for
macOS Exposé/Mission Control. The integrated right touchpad remains mouse
input; the left touchpad scrolls and its click acts as right-click.

The Go60 workflow builds the left and right halves into one `go60.uf2`
artifact using the official MoErgo ZMK distribution. Push the repository and
download that artifact from the **Build Go60 firmware** GitHub Actions run.
