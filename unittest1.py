import unittest
a=int(input())
result=[]

for i in range(a):
    var=list(map(int,input().split()))
    result.append(var)
for o in range(a):
    result[o]=result[o][::-1]
for j in range(0,len(result)):
    for g in range(0,len(result[0])):
        if result[j][g]==0:
            result[j][g]=1
        else:
            result[j][g]=0
for i in range(0,len(result)):
    for j in range(0,len(result[0])):
        print(result[i][j],end=" ")
    print()

# i --- IGNORE ---
#unit testing
class TestMatrixInversion(unittest.TestCase):
    def test_inversion(self):
        self.assertEqual(invert_matrix([[0,1],[1,0]]), [[1,0],[0,1]])
        self.assertEqual(invert_matrix([[1,0,0],[0,1,0],[0,0,1]]), [[0,1,1],[1,0,1],[1,1,0]])
def invert_matrix(matrix):
    inverted = []
    for row in matrix:
        inverted_row = []
        for val in row:
            if val == 0:
                inverted_row.append(1)
            else:
                inverted_row.append(0)
        inverted.append(inverted_row)
    return inverted
if __name__ == '__main__':
    unittest.main()
