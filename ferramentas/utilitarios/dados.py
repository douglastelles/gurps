#!/usr/bin/env python3
"""
Simulador de Dados para GURPS
Permite rolar dados no formato padrão do GURPS (ex: 3d6, 1d20, etc.)
"""

import random
import argparse
import re

def parse_dice(dice_string):
    """
    Parse uma string de dados no formato XdY
    Retorna (quantidade, faces)
    """
    match = re.match(r'(\d+)d(\d+)', dice_string.lower())
    if not match:
        raise ValueError(f"Formato inválido: {dice_string}. Use formato XdY (ex: 3d6)")
    
    quantidade = int(match.group(1))
    faces = int(match.group(2))
    
    return quantidade, faces

def roll_dice(dice_string):
    """
    Rola dados e retorna o resultado
    """
    quantidade, faces = parse_dice(dice_string)
    resultados = [random.randint(1, faces) for _ in range(quantidade)]
    total = sum(resultados)
    
    return {
        'dados': resultados,
        'total': total,
        'quantidade': quantidade,
        'faces': faces
    }

def main():
    parser = argparse.ArgumentParser(description='Simulador de dados para GURPS')
    parser.add_argument('dados', help='Dados para rolar (ex: 3d6, 1d20)')
    parser.add_argument('--vezes', '-n', type=int, default=1, help='Número de vezes para rolar')
    parser.add_argument('--detalhado', '-d', action='store_true', help='Mostrar detalhes de cada rolagem')
    
    args = parser.parse_args()
    
    print(f"Rolando {args.dados} {args.vezes} vez(es):")
    print("-" * 40)
    
    for i in range(args.vezes):
        resultado = roll_dice(args.dados)
        
        if args.detalhado:
            print(f"Rolagem {i+1}: {resultado['dados']} = {resultado['total']}")
        else:
            print(f"Rolagem {i+1}: {resultado['total']}")
    
    if args.vezes > 1:
        print("-" * 40)
        print(f"Total de todas as rolagens: {sum(roll_dice(args.dados)['total'] for _ in range(args.vezes))}")

if __name__ == "__main__":
    main() 