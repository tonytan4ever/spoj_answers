'''
Created on Jul 29, 2010

@author: CTtan
'''
def main():
    numberOfTest = int(raw_input())
    for testSequence in range(0,numberOfTest):
        numberOfContestant = int(raw_input())
        #initialize the better-than info
        iAmBetterThanInfo = {}
        for i in range(0,numberOfContestant):
            iAmBetterThanInfo[i+1] = []
        #loop through all the actual better than info
        for playerIter in range(0,numberOfContestant):
            #here, read a list of numbers and convert this list from string to integer
            playBetterInfo = map(int,raw_input().split())
            # j here only iters over playBetterInfo[1:], since the first number is essentially useless
            # may be for other type of language
            for j in playBetterInfo[1:]: iAmBetterThanInfo[j].append(playerIter+1)
        numberOfSets = 0
        #in order to find a set, someone has to better than everyone else
        for key in iAmBetterThanInfo.keys():
            if traversal(key,iAmBetterThanInfo,numberOfContestant,visited=[]):
                numberOfSets += 1
        print numberOfSets  
                    

def traversal(key,adjancentInfo,numberOfContestant,visited):
    #print "traversal inner...",numberOfContestant
    result = False
    if numberOfContestant == 1:
        return True
    else:        
        #if this step's next is dead, return not found
        if adjancentInfo[key] == []:
            return False
        visited.append(key)
        for worseChild in adjancentInfo[key]:
            if worseChild in visited:
                if len(adjancentInfo[key]) == 1:
                    visited.remove(key)
                continue
            else:
                #print "here, or once"
                result = result or traversal(worseChild,adjancentInfo,numberOfContestant-1,visited)
    return result
            

           
if __name__ == "__main__":
    main()                   
                
            
            
            
            
            