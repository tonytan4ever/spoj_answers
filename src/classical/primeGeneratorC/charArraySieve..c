#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
typedef unsigned long bignum;
void printPrime(bignum bn){
	static char buf[1000];
	sprintf(buf,"%ull",bn);
	buf[strlen(buf) - 2]  = '\0';
	printf("%s\n",buf);
}
void findPrimes(bignum lowerCandidate,bignum topCandidate){
     char* array = malloc(sizeof(unsigned char) * (topCandidate));
     
     int ss;
     for (ss = 0; ss <= topCandidate+1; ss++) *(array + ss) = 1;
     array[0] = 0; array[1] = 0;
     bignum thisFactor = 2;
     bignum lastSquare = lowerCandidate;
     while(thisFactor * thisFactor <= topCandidate){
        bignum mark = thisFactor + thisFactor;
        while(mark <= topCandidate){
            *(array + mark) = 0;
            mark += thisFactor;
        }
        /*Set thisFactor to next prime*/
        thisFactor++;
        while(*(array+thisFactor) == 0) thisFactor++;
        /*assert(thisFactor <= topCandidate)*/
    }
     for (; lastSquare <= topCandidate; lastSquare++){
        if (*(array+lastSquare)) printPrime(lastSquare);
    }
    free(array);
}

int main(int argc, char *argv[])
{
    int numberOfTestCases;
    scanf("%d", &numberOfTestCases);
    
    bignum lowerCandidates[numberOfTestCases];
    bignum topCandidates[numberOfTestCases];
    
    int testCasesNumber;
    for (testCasesNumber = 0; testCasesNumber < numberOfTestCases; testCasesNumber++){
        bignum lowerCandidate, topCandidate;
        scanf("%ul",&lowerCandidates[testCasesNumber]);
        scanf("%ul", &topCandidates[testCasesNumber]);
        /*if (argc > 1)
    		topCandidate = atoll(argv[1]);*/
        /*test();*/
       
    }
    for (testCasesNumber = 0; testCasesNumber < numberOfTestCases; testCasesNumber++){
        
    }
    for (testCasesNumber = 0; testCasesNumber < numberOfTestCases; testCasesNumber++){
       findPrimes(lowerCandidates[testCasesNumber],topCandidates[testCasesNumber]);
       printf("\n");
    }
    getchar();
    return 0;
}
