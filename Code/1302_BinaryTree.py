# https://leetcode.com/problems/deepest-leaves-sum/

class BinaryTree():
    def __init__(self, root):
        self.root = root
    
    def b_tree(self):
        tot_len = 0
        sub_lst = []
        out_str = ''

        for i in range(len(self.root)):
            lst_len = 2**i

            ## Se restan 2 posiciones de la siguiente sublista por cada Null
            if None in sub_lst:
                c_none = sub_lst.count(None)
                lst_len-=c_none*2

            ## se arman las sublistas por cada nivel 
            if i < 2:
                sub_lst = self.root[i:i+lst_len]
                tot_len += lst_len
                out_str+=f'lvl: {i} - sub_lst : {sub_lst}\n'
            else:
                sub_lst = self.root[tot_len : tot_len+lst_len]
                tot_len += lst_len
                out_str+=f'lvl: {i} - sub_lst : {sub_lst}\n'

            ## rompe cuando ya no "queden" sublistas por armar
            if tot_len == len(self.root):
                break

        return str(out_str), sub_lst

    def deepestLeavesSum(self):
        ## tomamos la lista de la última hoja
        lst = self.b_tree()[1]
        suma_lst = sum([i for i in lst if i != None])

        return f'Sum of values of its deepest leaves : {suma_lst}' 
    

root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
b_tree1 = BinaryTree(root)
print(b_tree1.b_tree()[0])
print(b_tree1.deepestLeavesSum())

print('--'*20,'\n')
root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
b_tree1 = BinaryTree(root)
print(b_tree1.b_tree()[0])
print(b_tree1.deepestLeavesSum())

