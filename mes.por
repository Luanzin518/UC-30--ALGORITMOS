programa
{
    funcao inicio()
    {
        inteiro mes

        escreva("Me fala o numero do mês (1 a 12):")
        leia(mes)

        se (mes == 1)
        {
            escreva("Janeiro - 31 dias")
        }
        senao se (mes == 2)
        {
            escreva("Fevereiro - 28 dias")
        }
        senao se (mes == 3)
        {
            escreva("Marco - 31 dias")
        }
        senao se (mes == 4)
        {
            escreva("Abril - 30 dias")
        }
        senao se (mes == 5)
        {
            escreva("Maio - 31 dias")
        }
        senao se (mes == 6)
        {
            escreva("Junho - 30 dias")
        }
        senao se (mes == 7)
        {
            escreva("Julho -31 dias")
        }
        senao se (mes == 8)
        {
            escreva("Agosto - 31 dias")
        }
        senao se (mes == 9)
        {
            escreva("Setembro - 30 dias")
        }
        senao se (mes == 10)
        {
            escreva("Outubro - 31 dias")
        }
        senao se (mes == 11)
        {
            escreva("Novembro - 30 dias")
        }
        senao se (mes == 12)
        {
            escreva("Dezembro - 31 dias")
        }
        senao
        {
            escreva("Mes invalido, confere ai.")
        }
    }
}
