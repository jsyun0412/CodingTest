#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int tmp = 0;
    tmp = n / 10;
    int answer = (n * 12000) + (k * 2000) - tmp * 2000;
    return answer;
}