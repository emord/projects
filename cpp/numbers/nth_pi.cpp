#include <gmpxx.h>

#include <string>
#include <cstdint>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

mpf_class factorial(uint64_t x) {
    mpf_class res(1, 1000);
    for (uint64_t i = 2; i <= x; ++i) {
        res *= i;
    }
    return res;
}

mpf_class fastpi(mpf_class x) {
    mpf_class res(0.0, 1000);
    mpf_class tmp, tmp2;
    mpf_class t(2);
    for (uint8_t k = 0; k < 100; ++k) {
        mpf_pow_ui(tmp2.get_mpf_t(), factorial(k).get_mpf_t(), 2);
        res += pow(2, k+1) * tmp2 / factorial(2 * k + 1);
    }
    return res;
}

int main(int arc, char *argv[]) {
    int precision = atoi(argv[1]);
    char x[precision + 2]; //Should change this to a non variable length array
    mpf_class pi(fastpi(255));

    gmp_snprintf(x, precision+2, "%.Ff", pi.get_mpf_t());
    printf("%s\n", x);
}
