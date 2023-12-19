from persistence import *

import sys

def main(args ):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            given_quan = int(splittedline[1])
            if(given_quan != 0):
                toPrint = repo.products.find(id = splittedline[0])  ##
               # print(toPrint[0].quantity)
                
                our_curr_product_quan = repo.products.find(id = splittedline[0])[0].quantity
                the_new_quan = int(given_quan) + our_curr_product_quan
                if(the_new_quan>=0):
                    repo.activities.insert(Activitie(*splittedline))
                    repo.products.update(the_new_quan,splittedline[0])
                      

if __name__ == '__main__':
    main(sys.argv)