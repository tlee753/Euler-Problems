#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int main() {
    struct timeval start, end;
    gettimeofday(&start, NULL);
    clock_t t0 = clock();
    
    int total = 0;
    
    for (int i=0; i<1000; i++) {
        if ( (i%3==0) || (i%5==0) ) {
            total += i;
        }
    }
    
    printf("%d\n", total); // prints answer
    clock_t t1 = clock();
    gettimeofday(&end, NULL);
    
    printf("--- %9.8f seconds ---\n", (float)  ((end.tv_sec/* + end.tv_usec/1000000*/ + end.tv_usec/1000000) - (start.tv_sec/* + start.tv_usec/1000000*/ + start.tv_usec/1000000)));
    printf("--- %g clocks ---\n", (double) (t1 - t0) );
    return 0;
}
