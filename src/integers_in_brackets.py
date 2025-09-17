#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    test1=(re.findall(r"\[\s*?([-]?[^a]?\d\d)\s?\]", s))
    test2= list(map(int, test1))
    #thing1=[]
    #for thing in test1:
        #thing.strip("+")
    #print(thing)
    #thing1.append(thing)
        #print_out=[]
        #print_out.append(s)
    return(test2)
    #return test1
    
    

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")) 
    #Output for the above should be: [12, -43, 12]

    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))
    #Output for the above should be: [47, 12]
    
    print(integers_in_brackets(""))
    #Output for the above should be: []
    
    

if __name__ == "__main__":
    main()
