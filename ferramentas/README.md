# Ferramentas

Esta pasta contém ferramentas, calculadoras e utilitários para facilitar o jogo.

## Estrutura Sugerida

### Calculadoras
- `calculadoras/` - Calculadoras automáticas
  - `combate.py` - Calculadora de combate
  - `dano.py` - Calculadora de dano
  - `magia.py` - Calculadora de magia

### Geradores
- `geradores/` - Geradores de conteúdo
  - `personagem.py` - Gerador de personagens
  - `npc.py` - Gerador de NPCs
  - `encontro.py` - Gerador de encontros

### Utilitários
- `utilitarios/` - Ferramentas diversas
  - `dados.py` - Simulador de dados
  - `tabelas.py` - Gerador de tabelas
  - `conversor.py` - Conversor de unidades

## Ferramentas Disponíveis

### Calculadora de Combate
```python
# Exemplo de uso
python calculadoras/combate.py --atacante "Guerreiro" --defensor "Orc" --arma "Espada"
```

### Gerador de Personagem
```python
# Exemplo de uso
python geradores/personagem.py --pontos 150 --tipo "Guerreiro"
```

### Simulador de Dados
```python
# Exemplo de uso
python utilitarios/dados.py --dados "3d6" --vezes 10
```

## Como Usar

1. **Calculadoras**: Para cálculos complexos durante o jogo
2. **Geradores**: Para criar conteúdo rapidamente
3. **Utilitários**: Para tarefas específicas

## Dependências

- Python 3.7+
- Bibliotecas: random, math, argparse

## Instalação

```bash
pip install -r requirements.txt
``` 