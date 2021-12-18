import sys
from types import SimpleNamespace as obj
from functools import reduce
from operator import mul


Literal = (lambda version, length, value:
    obj(
        type='Literal',
        version=version,
        length=length,
        value=value,
    ))

Operator = (lambda version, length, typeid, children:
    obj(
        type='Operator',
        version=version,
        length=length,
        typeid=typeid,
        children=children,
    ))


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    hexstring = f.read().strip()

    tree = parse(to_bits(hexstring))

    print(evaltree(tree))


def evaltree(tree):
    if tree.type == 'Literal':
        return tree.value
    elif tree.type == 'Operator':
        values = [evaltree(c) for c in tree.children]
        return evalop(tree.typeid, values)
    else:
        1/0


def evalop(typeid, values):
    if typeid == 0:
        return sum(values)
    elif typeid == 1:
        return reduce(mul, values)
    elif typeid == 2:
        return min(values)
    elif typeid == 3:
        return max(values)
    elif typeid == 5:
        return int(values[0] > values[1])
    elif typeid == 6:
        return int(values[0] < values[1])
    elif typeid == 7:
        return int(values[0] == values[1])
    else:
        1/0


def to_bits(hexstring):
    for ch in hexstring:
        nibble = int(ch, 16)
        bits = bin(nibble)[2:].zfill(4)
        for b in bits:
            yield int(b)


def parse(bits):  # bits is an iterator
    version = consume_bits(bits, 3)
    typeid = consume_bits(bits, 3)
    if typeid == 4:  # literal
        return parse_literal_node(bits, version)
    else:  # operator
        return parse_operator_node(bits, version, typeid)


def parse_operator_node(bits, version, typeid):  # bits is an iterator
    my_length = 6
    length_mode = consume_bits(bits, 1)
    my_length += 1
    if length_mode == 0:  # length is in bits
        limit = consume_bits(bits, 15)
        my_length += 15
        children_length = 0
        children = []
        while children_length < limit:
            child = parse(bits)
            children.append(child)
            children_length += child.length
        assert children_length == limit
        my_length += children_length
        return Operator(version, my_length, typeid, children)
    else:  # length is count of direct children
        limit = consume_bits(bits, 11)
        my_length += 11
        children_length = 0
        children = []
        while len(children) < limit:
            child = parse(bits)
            children.append(child)
            children_length += child.length
        my_length += children_length
        return Operator(version, my_length, typeid, children)


def parse_literal_node(bits, version):  # bits is an iterator
    value_bits = []
    is_continue = True
    my_length = 6
    while is_continue:
        is_continue = consume_bits(bits, 1)
        chunk = consume_bits(bits, 4, parseint=False)
        my_length += 5
        value_bits.extend(chunk)
    value = to_int(value_bits)
    return Literal(version, my_length, value)


def consume_bits(bits, n, *, parseint=True):  # bits is an iterator
    consumed = (next(bits) for _ in range(n))
    if parseint:
        return to_int(consumed)
    else:
        return list(consumed)


def to_int(bits_finite):
    return int(''.join(str(bit) for bit in bits_finite), 2)


if __name__ == '__main__':
    main()
