import fileinput, collections, collections as cl, itertools, itertools as it, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
import nodes


# i REALLY want to use the name 'bits' instead of e.g. 'bits_iter'
# would be nicer in a statically typed language

# TODO
# . consume-and-increment?
# . should version & typeid be in parse() or parse_*_node()?


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    hexstring = f.read().strip()

    print(parse(to_bits('D2FE28')))
    print(parse(to_bits('38006F45291200')))


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
        return parse_operator_node(bits, version)


def parse_operator_node(bits, version):  # bits is an iterator
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
        return nodes.Operator(version, my_length, children)
    else:  # length is count of direct children
        1/0


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
    return nodes.Literal(version, my_length, value)


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
