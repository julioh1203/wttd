'''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.

Os requisitos básicos são os seguintes:

a) Entregar o menor número de notas;
b) É possível sacar o valor solicitado com as notas disponíveis;
c) Saldo do cliente infinito;
d) Quantidade de notas infinito
e) Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.

'''

def dispenser(valor_saque):
    notas={}
    while valor_saque > 0:
        if valor_saque >= 100:
            notas['100'] = notas.get('100',0) + 1
            valor_saque = valor_saque - 100
        elif valor_saque >= 50:
            notas['50'] = notas.get('50',0) + 1
            valor_saque = valor_saque - 50
        elif valor_saque >= 20:
            notas['20'] = notas.get('20',0) + 1
            valor_saque = valor_saque - 20
        elif valor_saque >= 10:
            notas['10'] = notas.get('10',0) + 1
            valor_saque = valor_saque - 10

    return notas

if __name__ == '__main__':
    assert dispenser(30) == {'20': 1, '10': 1}
    assert dispenser(80) == {'50': 1, '20': 1, '10': 1}
    assert dispenser(120) == {'100': 1, '20': 1}
    assert dispenser(200) == {'100': 2}
    assert dispenser(1050) == {'100': 10, '50': 1}
    assert dispenser(480) == {'100': 4, '50': 1, '20':1, '10':1}