import sys

def read_format_input():
    K, M = sys.stdin.readline().split(' ')
    K,M = int(K), int(M)
    ls = []
    for i in range(int(K)):
         ls.append(clean_list(sys.stdin.readline()))
    print(ls)
        
def clean_list(line):
    line = line.split(' ')
    ls = [int(i) for i in line]
    return ls



if '__main__' == __name__:
    read_format_input()
