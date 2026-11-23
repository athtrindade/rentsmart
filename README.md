# RentSmart — Sistema de Orçamento de Locação (R.M Imóveis)

Aplicação em Python (Programação Orientada a Objetos) que calcula o orçamento de
locação de apartamentos, casas e estúdios, apresenta um resumo detalhado e gera um
CSV com a projeção dos 12 primeiros meses.

## Requisitos
- Python 3.8 ou superior (somente biblioteca padrão, **não precisa instalar nada**).

## Como executar
1. Extraia o arquivo zip.
2. Abra o terminal (ou prompt de comando) dentro da pasta `rentsmart`.
3. Execute:
   ```
   python main.py
   ```
   (no Linux/macOS, se necessário: `python3 main.py`)
4. Responda às perguntas. Ao final será criado o arquivo `projecao_12_meses.csv`
   na pasta atual (abre direto no Excel).

## Como rodar os testes
```
python tests/test_rentsmart.py
```

## Regras de negócio implementadas
| Item | Regra |
|---|---|
| Aluguel-base | Apartamento 1q: R$ 700 · Casa 1q: R$ 900 · Estúdio: R$ 1.200 |
| 2 quartos | Apartamento +R$ 200 · Casa +R$ 250 (estúdio só tem 1 quarto) |
| Garagem (casa/apto) | 1 vaga por +R$ 300/mês |
| Estacionamento (estúdio) | Pacote de 2 vagas R$ 250 + R$ 60 por vaga adicional |
| Desconto | Apartamento sem crianças: 5% sobre o aluguel já com adicionais |
| Taxa contratual | R$ 2.000, cobrada à parte, em 1 a 5 parcelas |

**Premissas adotadas:** o estacionamento do estúdio é opcional (0 vagas ou no mínimo 2);
na divisão da taxa, a última parcela absorve a diferença de centavos.

## Estrutura do projeto
```
rentsmart/
├── main.py                  # ponto de entrada
├── rentsmart/
│   ├── imoveis.py           # Imovel (abstrata), Apartamento, Casa, Estudio
│   ├── orcamento.py         # TaxaContratual e Orcamento
│   ├── projecao.py          # ProjecaoFinanceira (12 meses + CSV)
│   ├── interface.py         # entrada e validação de dados
│   └── formatacao.py        # formatação de moeda
└── tests/test_rentsmart.py  # testes automatizados
```

## Orientação a Objetos aplicada
- **Abstração/Herança:** `Imovel` define o contrato; `Apartamento`, `Casa` e `Estudio` herdam e especializam.
- **Polimorfismo:** cada tipo implementa suas regras de adicional de quartos, garagem e desconto, e o `Orcamento` trata todos da mesma forma.
- **Encapsulamento/Responsabilidade única:** cálculo (imóveis), cobrança (orçamento/taxa), exportação (projeção) e interação (interface) ficam em classes/módulos separados.
- Valores monetários usam `Decimal` para evitar erros de ponto flutuante.
