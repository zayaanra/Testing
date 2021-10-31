#include <stdio.h>
#include <stdlib.h>

#define ELEMS 5

/* Prototypes */
void *get_mem(size_t size);

int main(int argc, char *argv[]) {
    int *arr = (int*)get_mem(ELEMS);

    for(int i = 0; i<=ELEMS-1; i++) {
        arr[i] = i;
    }

    for(int j = 0; j<=ELEMS-1; j++) {
        printf("%d", arr[j]);
    }

    free(arr);
    return 0;
}

/* Return memory big enough to hold 5 elements */
void *get_mem(size_t size) {
    return calloc(size, sizeof(int));
}