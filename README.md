# Relatório Técnico — Extração e Cruzamento de Destinos (PyTravel)

## Descrição do Projeto

Este projeto foi desenvolvido para automatizar a leitura e o processamento de um catálogo de destinos turísticos em formato PDF, oferecido pela empresa fictícia **PyTravel**. O código extrai as informações de forma estruturada e realiza **cruzamentos entre categorias de destinos**.

O resultado final é apresentado em **formato Markdown**, facilitando a leitura e a inclusão em relatórios ou páginas web.

---

## Funcionamento do Código

O código realiza as seguintes etapas:

1. **Leitura do PDF** usando a biblioteca `PyMuPDF` (`fitz`);
2. **Extração de destinos** categorizados em 6 seções:
   - Cidades Praianas
   - Capitais
   - Cidades do Interior
   - Pacotes com Avião
   - Pacotes com Ônibus
   - Pacotes com Navio
3. **Cruzamento de informações** entre as categorias, como:
   - Capitais que são cidades praianas
   - Cidades do interior com pacotes de avião
   - Praianas com transporte por ônibus
   - Capitais com acesso por todos os meios de transporte
4. **Geração de relatório** em Markdown com os resultados dos cruzamentos.

---

## Bibliotecas Utilizadas

| Biblioteca | Função |
|------------|--------|
| [PyMuPDF (fitz)](https://pymupdf.readthedocs.io) | Leitura e extração de texto de arquivos PDF |

---

## Dificuldades Encontradas

- **Identificação correta das seções**: o título de cada categoria variava e precisava ser detectado com precisão.
- **Remoção do caractere `•`** das linhas para extrair corretamente o nome da cidade.

---

## Calendário de Desenvolvimento

| Etapa                               | Tempo Estimado | Tempo Real |
|------------------------------------|----------------|------------|
| Leitura e entendimento do PDF      | 1h             | 0h45min    |
| Escrita da função de extração      | 1h             | 2h         |
| Desenvolvimento dos cruzamentos    | 1h             | 1h         |
| Geração de markdown e testes       | 1h             | 1h         |
| Revisão final e documentação       | 0h30min        | 1h30min    |
| **Total Geral**                    | **4h30min**    | **6h15min**|

---

## Considerações Finais e Melhorias Futuras

O sistema cumpre com sucesso o objetivo de extrair e cruzar os destinos a partir do PDF. Ele é leve, modular e de fácil manutenção.

### Possíveis melhorias:
- Exportar os resultados para `.csv`, `.json` ou `.xlsx`;
- Integrar gráficos de interseção usando `matplotlib_venn` (opcional).

---

Desenvolvido por @Jonnypaiva - Aluno do Curso de Inteligência Artificial da Uniateneu
Com Orientação do Mestre @Sandromesquita