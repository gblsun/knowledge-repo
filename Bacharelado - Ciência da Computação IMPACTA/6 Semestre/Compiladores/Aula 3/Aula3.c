#include <stdio.h>

int main(void) {
    // ~ inverte cada bit de 10 (complemento de um): 0 vira 1, 1 vira 0.
    // 10 em 32 bits: 00000000 00000000 00000000 00001010
    // ~10:           11111111 11111111 11111111 11110101
    //
    // Como 'int' é assinado, esse padrão de bits é interpretado em
    // complemento de dois: o bit mais à esquerda (1) indica número negativo.
    // Regra prática: para inteiro assinado, ~n é sempre igual a -(n + 1).
    // Logo ~10 = -(10 + 1) = -11.
    int x = ~10;

    printf("%d\n", x); // imprime -11
    return 0;
}