
import random
import sys


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ('Enter in terminal like: python generate_fix.py number_of_messages_to_generate')
        exit(1)

    num_fix = int(sys.argv[1])
    

    fix_dict = {'54':['1','2'],
                '40':['1','2','3','4','5'],
                '59':['0','1','2','3','4','5','6'],
                '167':['FUT', 'OPT', 'CS']
                }
    file_name="output.txt"

    f = open(file_name, 'w')

    for _ in range(num_fix):

	    # symbol_n: product name 
        symbol_n = str(random.randint(1,10))

	    # value for buy or sell
        c_54 = random.choice(fix_dict['54'])

        # quantity of the symbol/product that buy or sell
        n_38 = str(random.randint(1,10000))

        #order_type
        c_40 = random.choice(fix_dict['40'])

        #all time in force
        c_59 = random.choice(fix_dict['59'])

        #Futures/optics
        c_167 = random.choice(fix_dict['167'])

        #client_n 
        client_n = str(random.randint(1,100000))

        #Any price 
        price = str(random.uniform(0, 10000))

        msg = '8=FIX.4.2|35=D|55=SYMBOL_'+symbol_n+'|54='+c_54+'|38='+n_38+'|40='+c_40
        msg += '|59='+c_59+'|167='+c_167+'|1=CLIENT_'+client_n+'|44='+price

        #print msg
        f.write(msg+'\n')


    f.close()