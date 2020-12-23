# Uses python3
import sys

def get_change(m):
    
    count = 0
    
    while m != 0 :
        if m % 4 == 0 :
            count += m // 4
            m = m % 4

        elif m % 3 == 0 and m <= 10 :
            m % 3 == 0 
            count += m // 3
            m = m % 3         
        elif m >= 4  :
            m = m - 4
            count += 1

        elif m >= 3  :
            m = m - 3
            count += 1
            
        else :
            count += m
            m -= m
           
               
                     
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
