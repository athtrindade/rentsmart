from rentsmart.interface import escolher_imovel, escolher_parcelas, ler_sim_nao
from rentsmart.orcamento import Orcamento, TaxaContratual
from rentsmart.projecao import ProjecaoFinanceira

ARQUIVO_CSV = "projecao_12_meses.csv"


def main() -> None:
    print("=== RentSmart | R.M Imóveis ===")
    while True:
        imovel = escolher_imovel()
        taxa = TaxaContratual(escolher_parcelas())
        orcamento = Orcamento(imovel, taxa)

        print()
        print(orcamento.resumo())

        caminho = ProjecaoFinanceira(orcamento).exportar_csv(ARQUIVO_CSV)
        print(f"\nProjeção de 12 meses salva em: {caminho}")

        if not ler_sim_nao("\nDeseja fazer outro orçamento?"):
            break
    print("Obrigado por usar o RentSmart!")


if __name__ == "__main__":
    main()
