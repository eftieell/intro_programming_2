def sum_of_k_numbers( k : int ) -> int:
    # find the sum of the integers up to and including k
    total = 0
    for number in range(k+1) :    # k+1 needed so we include k in the sum
        total += number
    return total

def sum_of_k_numbers_downward( k : int ) -> int:
    # find the sum of the integers up to and including k
    total = 0
    for number in range(k,0,-1) :  # 0 needed so we include 1 in the sum
        total += number
    return total

def sum_of_items( prices_of_items : list[float] ) -> float:
    # find the sum of the numbers in item_list
    total = 0
    for index in range( len( prices_of_items )) :
        total += prices_of_items[index]
    return total

def main() :
    print( sum_of_k_numbers( 10 ) )
    print( sum_of_k_numbers_downward( 10 ))
    print( sum_of_items( [1.0, 3.0, 2.5, 4.3]) )

if __name__ == '__main__' :
    main()