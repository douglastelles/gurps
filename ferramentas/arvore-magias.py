#!/usr/bin/env python3
"""
Árvore de Pré-requisitos de Magias - GURPS
Ferramenta para visualizar e navegar pelos pré-requisitos de magias
"""

import json
import argparse
from typing import Dict, List, Set

# Dados de exemplo - você pode expandir baseado nos seus PDFs
MAGIAS_EXEMPLO = {
    "Fogo": {
        "custo": 3,
        "prerequisitos": ["Magia Elemental"],
        "descricao": "Cria uma pequena chama"
    },
    "Bola de Fogo": {
        "custo": 5,
        "prerequisitos": ["Fogo", "Projetil"],
        "descricao": "Lança uma bola de fogo"
    },
    "Projetil": {
        "custo": 2,
        "prerequisitos": ["Magia Elemental"],
        "descricao": "Cria um projétil mágico"
    },
    "Magia Elemental": {
        "custo": 1,
        "prerequisitos": [],
        "descricao": "Base para magias elementais"
    },
    "Cura": {
        "custo": 4,
        "prerequisitos": ["Magia de Cura"],
        "descricao": "Cura ferimentos leves"
    },
    "Magia de Cura": {
        "custo": 1,
        "prerequisitos": [],
        "descricao": "Base para magias de cura"
    }
}

def carregar_magias(arquivo: str = None) -> Dict:
    """Carrega magias de arquivo JSON ou usa dados de exemplo"""
    if arquivo:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado. Usando dados de exemplo.")
            return MAGIAS_EXEMPLO
    return MAGIAS_EXEMPLO

def encontrar_caminho(magias: Dict, magia_destino: str, magia_atual: str = None, caminho: List[str] = None) -> List[str]:
    """Encontra o caminho de pré-requisitos para uma magia"""
    if caminho is None:
        caminho = []
    
    if magia_atual == magia_destino:
        return caminho + [magia_atual]
    
    if magia_atual in caminho:  # Evita loops
        return None
    
    if magia_atual:
        caminho.append(magia_atual)
    
    if magia_destino not in magias:
        return None
    
    prereqs = magias[magia_destino].get('prerequisitos', [])
    
    for prereq in prereqs:
        resultado = encontrar_caminho(magias, prereq, prereq, caminho.copy())
        if resultado:
            return resultado
    
    return None

def mostrar_arvore(magias: Dict, magia: str, nivel: int = 0):
    """Mostra a árvore de pré-requisitos de uma magia"""
    if magia not in magias:
        print(f"❌ Magia '{magia}' não encontrada!")
        return
    
    indentacao = "  " * nivel
    magia_info = magias[magia]
    
    print(f"{indentacao}📖 {magia}")
    print(f"{indentacao}   Custo: {magia_info['custo']} pontos")
    print(f"{indentacao}   Descrição: {magia_info['descricao']}")
    
    prereqs = magia_info.get('prerequisitos', [])
    if prereqs:
        print(f"{indentacao}   Pré-requisitos:")
        for prereq in prereqs:
            if prereq in magias:
                print(f"{indentacao}   └─ {prereq}")
                mostrar_arvore(magias, prereq, nivel + 2)
            else:
                print(f"{indentacao}   └─ ❌ {prereq} (não encontrada)")
    print()

def listar_magias_disponiveis(magias: Dict):
    """Lista todas as magias disponíveis"""
    print("📚 Magias Disponíveis:")
    print("-" * 40)
    for nome, info in magias.items():
        prereqs = ", ".join(info.get('prerequisitos', [])) or "Nenhum"
        print(f"• {nome} ({info['custo']} pts) - Pré-req: {prereqs}")
    print()

def main():
    parser = argparse.ArgumentParser(description='Árvore de Pré-requisitos de Magias - GURPS')
    parser.add_argument('--magia', '-m', help='Magia para mostrar a árvore')
    parser.add_argument('--listar', '-l', action='store_true', help='Listar todas as magias')
    parser.add_argument('--arquivo', '-f', help='Arquivo JSON com dados das magias')
    
    args = parser.parse_args()
    
    magias = carregar_magias(args.arquivo)
    
    if args.listar:
        listar_magias_disponiveis(magias)
        return
    
    if args.magia:
        print(f"🌳 Árvore de Pré-requisitos para '{args.magia}':")
        print("=" * 50)
        mostrar_arvore(magias, args.magia)
    else:
        print("🔮 Árvore de Pré-requisitos de Magias - GURPS")
        print("=" * 50)
        print()
        print("Uso:")
        print("  python arvore-magias.py --listar")
        print("  python arvore-magias.py --magia 'Bola de Fogo'")
        print()
        print("Exemplos de magias disponíveis:")
        for nome in list(magias.keys())[:5]:
            print(f"  • {nome}")

if __name__ == "__main__":
    main() 