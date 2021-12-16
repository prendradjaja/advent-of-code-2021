from types import SimpleNamespace as obj

Literal = (lambda version, length, value:
    obj(
        type='Literal',
        version=version,
        length=length,
        value=value,
    ))

Operator = (lambda version, length, children:
    obj(
        type='Operator',
        version=version,
        length=length,
        children=children,
    ))
