#include <stdlib.h>
#include <stdio.h>

int main ()
{
	float peso, altura, resultado;

	printf("Bem vindo a calculadora de IMC programada em C, feito por GABRIEL MUCHON PAVANELLI.\n");

	printf(" Digite seu peso:");
	scanf("%f", &peso);

	printf(" Digite sua altura:");
	scanf("%f", &altura);

    resultado = peso/(altura*altura);

    printf("Seu IMC é:%f", resultado);

}
