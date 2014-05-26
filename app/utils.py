# -*- coding: utf-8 -*-

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]


def improve_dump(fname):
    suffix = ');\n'
    section_card = 4
    size = 19
    with open(fname, 'rb') as f:
        content = f.readlines()

    result = []

    for line in content:
        parts = line.split(',')
        if len(parts) < 4:
            continue

        if len(parts[-1]) > 5:
            card_no = parts[-1].split(suffix)[0]
            card_no = card_no[::-1]
            sections = []
            for chunk in chunks(card_no, section_card):
                sections.append(chunk)

            card_no = ' '.join(reversed(sections))
            card_no = ' ' + '0' * (section_card - len(sections[-1])) + card_no
            card_no = '0' * (size - len(card_no)) + card_no
            templated = "'" + card_no + "'" + suffix
        else:
            templated = "''" + suffix
        parts = parts[:-1]
        parts.append(templated)

        result.append(','.join(parts))

    print len(result)
    with open('../metadata/produced.sql', 'wb') as f:
        f.writelines(result)


if __name__ == '__main__':
    pass