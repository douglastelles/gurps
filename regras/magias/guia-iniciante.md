# Guia para Iniciantes - Sistema de Magias GURPS

## 🎯 Introdução

Este guia foi criado para ajudar iniciantes a entender o sistema de magias do GURPS de forma clara e organizada.

## 📚 Conceitos Básicos

### O que é Magia no GURPS?
- **Magia** é uma perícia especial que permite usar poderes sobrenaturais
- Cada magia tem um **custo em pontos** e **pré-requisitos**
- Magias são organizadas em **escolas** (elemental, cura, proteção, etc.)

### Pontos de Magia
- **Pontos de Magia** são gastos ao usar magias
- Recuperam com **descanso** ou **itens mágicos**
- Quanto mais pontos, mais magias você pode usar

### Pré-requisitos
- Algumas magias precisam de outras como **base**
- Formam uma **árvore de dependências**
- Exemplo: Para aprender "Bola de Fogo", você precisa saber "Fogo" primeiro

## 🚀 Primeiros Passos

### 1. Escolha uma Escola
**Recomendado para iniciantes:**
- **Elemental**: Fogo, água, terra, ar
- **Cura**: Restauração de ferimentos
- **Proteção**: Escudos e defesas

### 2. Aprenda Magias Básicas
**Comece com magias simples:**
- **Fogo** (3 pontos) - Cria uma pequena chama
- **Cura** (4 pontos) - Cura ferimentos leves
- **Escudo** (3 pontos) - Cria proteção mágica

### 3. Entenda os Pré-requisitos
**Use a ferramenta de árvore:**
```bash
python ferramentas/arvore-magias.py --listar
python ferramentas/arvore-magias.py --magia "Bola de Fogo"
```

## 📊 Como Usar Magias

### Passo a Passo
1. **Escolha a magia** que quer usar
2. **Verifique se tem pontos** suficientes
3. **Faça teste de perícia** da magia
4. **Gaste pontos** se conseguir
5. **A magia acontece** conforme descrição

### Exemplo Prático
**Usando "Fogo":**
- Custo: 3 pontos de magia
- Teste: Perícia "Fogo" vs dificuldade
- Efeito: Cria uma pequena chama
- Duração: Instantânea

## 🎮 Dicas para Iniciantes

### Durante o Jogo
- **Comece simples**: Use magias básicas primeiro
- **Conserve pontos**: Não gaste tudo de uma vez
- **Pratique**: Use magias regularmente para melhorar
- **Combine**: Use magias em conjunto

### Criação de Personagem
- **Invista em magia**: Coloque pontos em perícias mágicas
- **Escolha uma escola**: Foque em uma área primeiro
- **Planeje**: Veja a árvore de pré-requisitos
- **Equilibre**: Não esqueça de outras habilidades

## 🔧 Ferramentas Úteis

### Árvore de Pré-requisitos
```bash
# Listar todas as magias
python ferramentas/arvore-magias.py --listar

# Ver árvore de uma magia específica
python ferramentas/arvore-magias.py --magia "Bola de Fogo"
```

### Calculadora de Magia
```bash
# Calcular custo de magia
python ferramentas/calculadora-magica.py --magia "Fogo" --nivel 3
```

## 📖 Próximos Passos

### Para Aprofundar
1. **Leia o PDF original**: `documentos-originais/modulo-magias.pdf`
2. **Explore outras escolas**: Tente magias diferentes
3. **Crie combinações**: Combine magias para efeitos únicos
4. **Participe de discussões**: Troque experiências com outros jogadores

### Recursos Adicionais
- **Regras básicas**: `regras/basico/magia.md`
- **Tabelas de referência**: `regras/referencias/tabelas-magia.md`
- **Exemplos práticos**: `aventuras/exemplos/uso-magias.md`

## ❓ Perguntas Frequentes

**Q: Quantos pontos de magia devo ter?**
A: Para iniciantes, 10-20 pontos é suficiente.

**Q: Posso usar magias sem pré-requisitos?**
A: Não, você precisa aprender as magias base primeiro.

**Q: Como recupero pontos de magia?**
A: Com descanso, itens mágicos ou perícias especiais.

**Q: Posso combinar magias?**
A: Sim, mas cada magia precisa ser lançada separadamente. 