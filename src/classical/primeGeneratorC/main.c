#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
typedef unsigned long long bignum;
typedef struct{
    unsigned int *p;      /* pointer to array */
    int bitsPerByte;      /* 8 on normal systems*/
    int bytesPerInt;      /* sizeof(unsigned int) */
    int bitsPerInt;          /* for bit arithmetic */
    int bpiShift;            /* 8 bit words = 3, 16 = 4, etc*/
    int bpiMask;             /* bitsPerint - 1*/
    bignum bitsInArray;      /* how many bits in array */
    bignum intsInArray;      /* how many units to give necessary bits */
} BITARRAY;
void freeBitArray(BITARRAY *ba){
    free(ba->p);
    free(ba);
}
BITARRAY* createBitArray(bignum bits){
    BITARRAY* ba = malloc(sizeof(BITARRAY));
    /*assert(ba != NULL);*/
    ba->bitsPerByte = 8;
    ba->bytesPerInt = sizeof(unsigned int);
    ba->bitsPerInt = ba->bitsPerByte * ba->bytesPerInt;
    switch (ba->bitsPerInt){
        case 8: ba->bpiShift = 3; break;
        case 16: ba->bpiShift = 4; break;
        case 32: ba->bpiShift = 5; break;
        case 64: ba->bpiShift = 6; break;
        case 128: ba->bpiShift = 7; break;
        case 256: ba->bpiShift = 8; break;
        case 512: ba->bpiShift = 9; break;
        default: {
            perror("ABORTING: Non-standard bits per int\n");
            exit(1);
            break;
        }
    }
    ba->bpiMask = ba->bitsPerInt - 1;
    ba->bitsInArray = bits;
    ba->intsInArray = bits / ba->bitsPerInt + 1;
    ba->p = malloc(ba->intsInArray * ba->bytesPerInt);
    /*assert(ba->p != NULL);*/
    return ba;
}
void setBit(BITARRAY* ba, bignum bitSS){
    unsigned int *pInt = ba->p + (bitSS >> ba->bpiShift);
    unsigned int remainder = (bitSS & ba->bpiMask);
    *pInt |= (1 << remainder);
}
void clearBit(BITARRAY* ba, bignum bitSS){
    unsigned int *pInt = ba->p + (bitSS >> ba->bpiShift);
    unsigned int remainder = (bitSS & ba->bpiMask);
    unsigned int mask = 1 << remainder;
    mask = ~mask;
    *pInt &= mask;
}
int getBit(BITARRAY* ba, bignum bitSS){
    unsigned int *pInt = ba->p + (bitSS >> ba->bpiShift);
    unsigned int remainder = (bitSS & ba->bpiMask);
    unsigned int ret = *pInt;
    ret &= (1<<remainder);
    return (ret != 0);
}
void clearAll(BITARRAY *ba){
    bignum intSS;
    for(intSS=0; intSS <= ba->intsInArray; intSS++){
        *(ba->p + intSS) = 0;
    }
}
void setAll(BITARRAY *ba){
    bignum intSS;
    for(intSS=0; intSS <= ba->intsInArray; intSS++){
        *(ba->p + intSS) = ~0;
    }
}
void printPrime(bignum bn){
	static char buf[1000];
	sprintf(buf,"%ull",bn);
	buf[strlen(buf) - 2]  = '\0';
	printf("%s\n",buf);
}
void findPrimes(bignum topCandidate){
    BITARRAY* ba = createBitArray(topCandidate);
    /*assert(ba != NULL);*/
    /* Set all but 0 and 1 to prime status*/
    setAll(ba);
    clearBit(ba, 0);
    clearBit(ba, 1);
    /* Mark all the non-primes */
    bignum thisFactor = 2;
    bignum lastSquare = 0;
    bignum thisSquare = 0;
    while(thisFactor * thisFactor <= topCandidate){
        /* Mark the multiples of this factor */
        bignum mark = thisFactor + thisFactor;
        while(mark <= topCandidate){
            clearBit(ba,mark);
            mark += thisFactor;
        }
        /* Print the proven primes so far*/
        thisSquare = thisFactor * thisFactor;
        for(;lastSquare < thisSquare; lastSquare++){
            if(getBit(ba,lastSquare)) printPrime(lastSquare);
        }
        /*Set thisFactor to next prime*/
        thisFactor++;
        while(getBit(ba, thisFactor) == 0) thisFactor++;
        /*assert(thisFactor <= topCandidate)*/
    }
    /*print the remaining primes*/
    for (; lastSquare <= topCandidate; lastSquare++){
        if (getBit(ba,lastSquare)) printPrime(lastSquare);
    }
    freeBitArray(ba);
}
void test(){
    int ss;
    BITARRAY* ba = createBitArray(77);
    clearAll(ba);
    /*setAll(ba)*/
    setBit(ba,0);
    setBit(ba,64);
    setBit(ba,10);
    clearBit(ba,10);
    clearBit(ba,0);
    setBit(ba,64);
    setBit(ba,10);
    setBit(ba,0);
    for(ss=0; ss<78; ss++){
        if(getBit(ba,ss) != 0){
            printf("%d",ss);
            printf("=%d ON!!!",(getBit(ba,ss)));
            printf("\n");
        }
    }
    printf("First int is %ull.\n", *(ba->p));
}
int main(int argc, char *argv[])
{
    bignum topCandidate = 1000;
	if (argc > 1)
		topCandidate = atoll(argv[1]);
    /*test();*/
	findPrimes(topCandidate);
	getchar();
    return 0;
}
