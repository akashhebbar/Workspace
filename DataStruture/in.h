#define MAX_SIZE 10
void insertion(int fn_arr[]) {
    int i, j, a, t;
    for (i = 1; i < MAX_SIZE; i++) {
        t = fn_arr[i];
        j = i - 1;

        while (j >= 0 && fn_arr[j] > t) {
            fn_arr[j + 1] = fn_arr[j];
            j = j - 1;
        }

        fn_arr[j + 1] = t;

        printf("\nIteration %d : ", i);
        for (a = 0; a < MAX_SIZE; a++) {
            printf("\t%d", fn_arr[a]);
        }
    }

    printf("\n\nSorted Data :");
    for (i = 0; i < MAX_SIZE; i++) {
        printf("\t%d", fn_arr[i]);
    }
}
