/*acc 0.07
Doubt if this is the known fasted version
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <assert.h>
#define msetBit(ba, bitSS) \
        { \
        *(ba + (bitSS >> 3)) |= \
        (1 << (bitSS & 7)); \
        }
#define mclearBit(ba, bitSS) \
	{ \
    *(ba + (bitSS >> 3)) &= \
    ~(1 << (bitSS & 7)); \
    }
    
#define mgetBit(ba, bitSS) \
        ( \
        ( \
        0 != \
       	( \
           	*(ba + (bitSS >> 3)) & \
               	(1 << (bitSS & 7)) \
                   	) \
        ) \
        )

typedef unsigned long bignum;
void printPrime(bignum bn){	
     static char buf[12];	
     sprintf(buf, "%ull", bn);	
     buf[strlen(buf) - 2] = '\0';	
     printf("%s\n", buf);	
}

int main(int argc, char *argv[])
{
    /*find all primes below 32000*/
    char primes[4000];
    bignum intSS;	
    memset(primes,~0,sizeof(primes));
    bignum thisFactor = 2;
    mclearBit(primes, 0); mclearBit(primes, 1);		
    while(thisFactor * thisFactor <= 31999) {		
         /* MARK THE MULTIPLES OF THIS FACTOR */		
         bignum mark = thisFactor + thisFactor;		
         while(mark <= 31999){			
             mclearBit(primes, mark);			
             mark += thisFactor;			
         }				
         /* SET thisFactor TO NEXT PRIME */		
         thisFactor++;		
         while(mgetBit(primes, thisFactor) == 0) thisFactor++;		
         /*assert(thisFactor <= 32000);*/		
     }
     
     /*int lastSquare = 0;
     for(;lastSquare <= 100; lastSquare++)	{		
        if(mgetBit(primes, lastSquare)) printPrime(lastSquare);		
     }*/
     
    /* Use Era Sieve on the given range */
    int T;
    scanf("%d", &T);
    
    bignum lowerCandidates[T];
    bignum topCandidates[T];
    
    for (intSS = 0; intSS < T; intSS++){
        if (intSS) printf("\n");
        bignum lowerCandidate, topCandidate;
        scanf("%ul",&lowerCandidates[intSS]);
        scanf("%ul", &topCandidates[intSS]);
        if (lowerCandidates[intSS] < 2)
    		lowerCandidates[intSS] = 2; 
        /*printf("%d, %d\n",lowerCandidates[intSS],topCandidates[intSS]);*/
        
        char isprime[100000/8];
        memset(isprime,~0,sizeof(isprime));
        bignum cap = sqrt(topCandidates[intSS]) + 1; 
        bignum primeSift;
        /*if the range is inside the known prime array, then just print it */
        if(topCandidates[intSS] <= 32199){
           int i;
           for (i = lowerCandidates[intSS]; i <= topCandidates[intSS]; i++) {
               if (mgetBit(primes, i)) {
                  printf("%d\n",i);
                }
            }
            continue;
        }
        
        for (primeSift = 2; primeSift <= 31999; primeSift++){
            if (primeSift >= cap) break;
            if (! mgetBit(primes, primeSift)) continue;
            
            /*start: index of the very first multiple of this prime inside the range
            */
            bignum start;
            if (primeSift >= lowerCandidates[intSS]) start = (primeSift)*2;
            else start = lowerCandidates[intSS] + ((primeSift - lowerCandidates[intSS] % primeSift) %primeSift) ;
            
            bignum j;
            for (j = start; j <= topCandidates[intSS]; j += primeSift) {
                mclearBit(isprime, j-lowerCandidates[intSS]);
            }
        }
        bignum i;
        for (i = lowerCandidates[intSS]; i <= topCandidates[intSS]; i++) {
            if (mgetBit(isprime, i-lowerCandidates[intSS])) {
                printf("%d\n",i);
            }
        }    
    }
  
    return 0;
}
