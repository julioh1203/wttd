"""
Determinar se um ano é bissexto obedecendo se:
a) Ele é divísel por 4;
b) Não é divisível por 100;
c) Porém, pode ser divísel por 400 também.

Exemplos:

1600 é bissexto

2011 não é bissexto

"""

def divisible_by_100(num):
    return num % 100 == 0

def divisible_by_400(num):
    return num % 400 == 0

def divisible_by_4(num):
    return num % 4 == 0

def bissexto(ano):
    tipo_ano='ano não é bissexto'
    if divisible_by_100(ano):
        if divisible_by_400(ano):
            tipo_ano='bissexto'
        #else:
        #    tipo_ano='ano não é bissexto'
    elif divisible_by_4(ano):
        tipo_ano='bissexto'
    #else:
    #   tipo_ano='ano não é bissexto'
    return tipo_ano
'''
    if ano == 1600:
        return 'bissexto'
    if ano == 2011:
        return 'ano não é bissexto'
    if ano == 1500:
        return 'ano não é bissexto'
'''

if __name__ == '__main__':
    assert bissexto(1600) == 'bissexto'
    assert bissexto(2016) == 'bissexto'
    assert bissexto(2011) == 'ano não é bissexto'
    assert bissexto(1900) == 'ano não é bissexto'
    assert bissexto(2000) == 'bissexto'
    assert bissexto(2004) == 'bissexto'
    assert bissexto(1640) == 'bissexto'
    assert bissexto(1658) == 'ano não é bissexto'
    assert bissexto(2015) == 'ano não é bissexto'
    assert bissexto(1975) == 'ano não é bissexto'