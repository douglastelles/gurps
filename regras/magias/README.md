# Sistema de Magias - GURPS

Esta seção contém informações organizadas sobre o sistema de magias do GURPS, extraídas dos PDFs originais.

## 📁 Estrutura

### Magias por Escola
- `elemental/` - Magias elementais (Fogo, Água, Terra, Ar)
- `cura/` - Magias de cura e restauração
- `protecao/` - Magias de proteção e escudos
- `comunicacao/` - Magias de comunicação e informação
- `movimento/` - Magias de movimento e teletransporte

### Ferramentas
- `arvore-prerequisitos.md` - Árvore visual de pré-requisitos
- `calculadora-magica.md` - Calculadora de custos de magia
- `guia-iniciante.md` - Guia para iniciantes no sistema de magia

## 🎯 Para Iniciantes

### Primeiros Passos
1. **Escolha uma escola**: Comece com uma escola de magia
2. **Aprenda magias básicas**: Magias de nível 1-2
3. **Entenda pré-requisitos**: Use a árvore de pré-requisitos
4. **Pratique**: Use magias simples primeiro

### Escolas Recomendadas para Iniciantes
- **Elemental**: Magias de fogo e água
- **Cura**: Magias de restauração
- **Proteção**: Magias defensivas

## 📊 Sistema de Magias

### Pontos de Magia
- Cada magia tem um custo em pontos
- Pontos são gastos ao usar a magia
- Recuperam com descanso ou itens

### Pré-requisitos
- Algumas magias precisam de outras como base
- Formam uma árvore de dependências
- Use a ferramenta `arvore-magias.py` para visualizar

### Casting
- Teste de perícia da magia
- Modificadores baseados na situação
- Custo de energia para usar

## 🔧 Ferramentas Disponíveis

### Árvore de Pré-requisitos
```bash
python ferramentas/arvore-magias.py --listar
python ferramentas/arvore-magias.py --magia "Bola de Fogo"
```

### Calculadora de Magia
```bash
python ferramentas/calculadora-magica.py --magia "Fogo" --nivel 3
```

## 📚 Referências

- **PDF Original**: `documentos-originais/modulo-magias.pdf`
- **Regras Básicas**: `regras/basico/magia.md`
- **Tabelas**: `regras/referencias/tabelas-magia.md` 