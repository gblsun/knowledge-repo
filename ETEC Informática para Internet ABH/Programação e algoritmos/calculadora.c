#include <stdlib.h>
#include <stdio.h>

int main ()
{
	float numero1, numero2, escolha, resultado;

	printf("Bem vindo a calculadora programada em C, feito por GABRIEL MUCHON PAVAN0ELLI.\n");

	printf(" Digite o primeiro numero.");
	scanf("%f", &numero1);

	printf("Digite o segundo numero.");
	scanf("%f", &numero2);

	printf ("Digite 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão e 5 para cancelar. ");
    scanf("%f", &escolha);

    if(escolha == 1)
    {
        resultado = numero1+numero2;

        printf ("O resultado dessa conta é: %f", resultado);
    }
    if (escolha == 2)
    {
        resultado = numero1-numero2;

        printf ("O resultado dessa conta é: %f", resultado);
    }
    if (escolha == 3)
    {
        resultado = numero1*numero2;

        printf ("O resultado dessa conta é: %f", resultado);
    }
      if (escolha == 4)
    {
        resultado = numero1/numero2;

        printf ("O resultado dessa conta é: %f", resultado);
    }
      if (escolha == 5)
    {
        printf ("Cancelado!");
    }
          if (escolha >= 5)
    {
        printf ("Número incorreto ou diferente do que foi pedido");
    }
          if (escolha <= 0)
    {
        printf ("Número incorreto ou diferente do que foi pedido");
    }

}
