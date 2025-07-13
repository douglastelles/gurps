# GURPS Workspace

Este workspace está organizado para gerenciar recursos e materiais relacionados ao GURPS (Generic Universal RolePlaying System), com foco especial em facilitar o acesso às informações dos PDFs originais.

## Estrutura do Projeto

### 📁 Documentos Originais
- PDFs originais do GURPS para consulta completa
- Módulo Básico e Módulo de Magias
- Referência completa quando necessário

### 📁 Personagens
- Fichas de personagens dos jogadores
- Templates de personagens
- Históricos e backgrounds

### 📁 Regras
- Regras básicas e avançadas organizadas
- Sistema de magias com guias para iniciantes
- Referências rápidas extraídas dos PDFs

### 📁 Aventuras
- Campanhas em andamento
- Módulos de aventuras
- Encontros e NPCs

### 📁 Mundo
- Cenários e settings
- Lore e história
- Mapas e localizações

### 📁 Ferramentas
- Árvore de pré-requisitos de magias
- Calculadoras de combate
- Geradores de personagens
- Utilitários diversos

### 📁 Recursos
- Materiais de referência
- Imagens e mapas
- Links úteis

## Como Usar

1. **Documentos Originais**: Consulte os PDFs para informações completas
2. **Personagens**: Crie uma pasta para cada jogador ou grupo
3. **Regras**: Use as versões organizadas para consulta rápida
4. **Aventuras**: Organize por campanha ou sessão
5. **Mundo**: Desenvolva o cenário de forma estruturada
6. **Ferramentas**: Use para cálculos e geração de conteúdo
7. **Recursos**: Armazene materiais de referência

## Ferramentas Especiais

### Árvore de Pré-requisitos de Magias
```bash
# Listar todas as magias disponíveis
python ferramentas/arvore-magias.py --listar

# Ver árvore de pré-requisitos de uma magia
python ferramentas/arvore-magias.py --magia "Bola de Fogo"
```

### Simulador de Dados
```bash
# Rolar dados no formato GURPS
python ferramentas/utilitarios/dados.py 3d6
python ferramentas/utilitarios/dados.py 1d20 --vezes 5 --detalhado
```

## Dicas

- Use nomes descritivos para arquivos e pastas
- Mantenha backups regulares
- Documente mudanças importantes
- Compartilhe recursos com os jogadores conforme necessário 