#include <iostream> 
#include <vector>
#include <map> 
#include <cmath>
#include <set>
 
using namespace std; 
typedef unsigned long bignum;
 
template<typename T = int, typename M = map<T, T> > 
class prime_iterator { 
    public: 
        prime_iterator() : current(2), skips() { skips[4] = 2; } 
        T operator*() { return current; } 
        prime_iterator &operator++() { 
            typename M::iterator i; 
            while ((i = skips.find(++current)) != skips.end()) { 
                T skip = i->second, next = current + skip; 
                skips.erase(i); 
                for (typename M::iterator j = skips.find(next); 
                        j != skips.end(); j = skips.find(next += skip)) {} 
                skips[next] = skip; 
            } 
            skips[current * current] = current; 
            return *this; 
        } 
    private: 
        T current; 
        M skips; 
}; 
 
int main() {
    //generate all primes up to 32000, saved in a global vector
    vector<int> primes;
    prime_iterator<int> initPrimes;
    for (; *initPrimes < 32000; ++initPrimes){ 
             primes.push_back(*initPrimes);
    }   
    
     
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
       if (testCasesNumber)  printf("\n");
       if (lowerCandidates[testCasesNumber] < 2) lowerCandidates[testCasesNumber]= 2;
       int cap = sqrt(topCandidates[testCasesNumber]) + 1;
       
       
       set<int> notprime;
       notprime.clear();
 
       vector<int>::iterator p;
       for (p = primes.begin(); p != primes.end(); p++) { 
            if (*p >= cap) break;
            //start: index of the very first multiple of this prime inside the range
            int start;
            if (*p >= lowerCandidates[testCasesNumber]) start = (*p)*2;
            else start = lowerCandidates[testCasesNumber] + ((*p - lowerCandidates[testCasesNumber] % *p) %*p) ;
 
            for (int j = start; j <= topCandidates[testCasesNumber]; j += *p) {
                notprime.insert(j);
            }
        }
 
        for (int i = lowerCandidates[testCasesNumber]; i <= topCandidates[testCasesNumber]; i++) {
            if (notprime.count(i) == 0) {
                printf("%d\n",i);
            }
        }       
    }
	return 0;	
}
