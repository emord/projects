#include <iostream>
#include <cstdint>

using namespace std;

uint64_t fib_recursive(uint64_t n) {
    if (n < 2)
        return 1;
    else
        return fib_recursive(n - 1) + fib_recursive(n - 2);
}

uint64_t fib_iterative(uint64_t n) {
    uint64_t a = 1, b = 1, index = 1;

    while (index < n) {
        b += a;
        a = b - a;
        ++index;
    }

    return b;
}

int main() {
    for (uint8_t i = 0; i < 20; ++i) {
        cout << fib_iterative(i) << endl;
        cout << fib_recursive(i) << endl;
    }
}
