# /// script
# dependencies = ["pyyaml"]
# ///
"""Reshape a keymap-drawer YAML from 3x6+3 (corne shield matrix) to 3x5+3
(physical chocofi layout) by dropping the outer NONE columns and remapping
combo positions. Reads from stdin, writes to stdout."""

import sys
import yaml

DROP = {0, 11, 12, 23, 24, 35}
REMAP = {old: new for new, old in enumerate(p for p in range(42) if p not in DROP)}

DROP_ELEMENT = {0: 0, 1: -1, 2: 0, 3: -1, 4: 0, 5: -1}


def reshape_layers(layers):
    out = {}
    for name, rows in layers.items():
        new_rows = []
        for i, row in enumerate(rows):
            if i not in DROP_ELEMENT:
                new_rows.append(row)
            elif DROP_ELEMENT[i] == 0:
                new_rows.append(row[1:])
            else:
                new_rows.append(row[:-1])
        out[name] = new_rows
    return out


def reshape_combos(combos):
    if not combos:
        return combos
    out = []
    for c in combos:
        new_c = dict(c)
        if 'p' in new_c:
            new_c['p'] = [REMAP[p] for p in new_c['p']]
        out.append(new_c)
    return out


def main():
    data = yaml.safe_load(sys.stdin)
    data['layout'] = {'ortho_layout': {'split': True, 'rows': 3, 'columns': 5, 'thumbs': 3}}
    if 'layers' in data:
        data['layers'] = reshape_layers(data['layers'])
    if 'combos' in data:
        data['combos'] = reshape_combos(data['combos'])
    yaml.safe_dump(data, sys.stdout, sort_keys=False, default_flow_style=None, width=200)


if __name__ == '__main__':
    main()
