## Layers (no combos)

![Layers](visualization/chocofi-keys.svg)

## Layers with combos

![Layers with combos](visualization/chocofi.svg)

## Go60

`config/go60.keymap` is a Go60 port of the Chocofi layout. It intentionally
uses only the Chocofi-compatible 36-key footprint: three five-key rows per
side plus six thumb keys. The Go60 number row, outer columns, and extra lower
keys are inert. It keeps the QWERTY, NUM, SYM, NAV, and SET layers, the six
thumb-key layer controls, Mac modifiers, and the Chocofi combos translated to
Go60 key positions. The right home-row punctuation key is apostrophe, and the
right bottom-row key is Backspace.

The physical MoErgo key is intentionally unused in this 36-key configuration,
so the Magic/status layer is reserved but not exposed from Base. The
integrated right touchpad remains mouse input; the left touchpad scrolls and
its click acts as right-click.

The Go60 workflow builds the left and right halves into one `go60.uf2`
artifact using the official MoErgo ZMK distribution. Push the repository and
download that artifact from the **Build Go60 firmware** GitHub Actions run.
