class Matrix:
    
    #define the value
    def __init__(self,dim,value):
        self.row=dim[0]
        self.col=dim[1]
        if isinstance(value,int) or isinstance(value,float):
            self.M= [ [value] * self.col for i in range (self.row) ]
        elif isinstance(value,list):
            self.M = value  
            
    #print matrix        
    def __str__(self):
        output=''
        for i in range(self.row):
            for j in range (self.col):
                output += str(self.M[i][j])
                if j!=self.col-1:
                    output+=' '
            output+='\n'
        return output   
    
    #add matrix
    def __add__(self,other):
        add_matrix=Matrix(dim=(self.row,self.col),value=0)
        
        if isinstance(other,Matrix):
            if self.row!=other.row or self.col!=other.col:
                print("two matrix don't have same size")
                return 0    
            for i in range(self.row):    
                for j in range (self.col):
                    add_matrix.M[i][j]=self.M[i][j]+other.M[i][j]     
                    
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(self.row):    
                for j in range (self.col):
                    add_matrix.M[i][j]=self.M[i][j]+other

        return add_matrix
    
    #minus matrix
    def __sub__(self,other):
        minus_matrix=Matrix(dim=(self.row,self.col),value=0)
        
        if type(other)==Matrix:
            if self.row!=other.row or self.col!=other.col:
                print("two matrix don't have same size")
                return
            for i in range(self.row):    
                for j in range (self.col):
                    minus_matrix.M[i][j] = self.M[i][j] - other.M[i][j]
        elif type(other)==int or float:
            for i in range(self.row):    
                for j in range (self.col):
                    minus_matrix.M[i][j] = self.M[i][j]- other
        return minus_matrix
    
    #matrix multiply matrix
    def __matmul__(self,other):
        if self.col != other.row :
            print("two matrix cannot multiply ")
            return 0
        multiply_matrix = Matrix(dim=(self.row,other.col),value=0)
        for i in range(self.row):
            for j in range (other.col):
                t=0 
                for k in range(self.col):
                    t = t + self.M[i][k] * other.M[k][j]
                multiply_matrix.M[i][j] = t    
        return multiply_matrix
    
    #transpose matrix
    def transpose(self):
        T_matrix=Matrix(dim=(self.col,self.row),value=0)
        for i in range(self.row):    
            for j in range (self.col):
                T_matrix.M[j][i]=self.M[i][j]     
        return T_matrix

    # multiply 
    def __mul__(self,other):
        mul_matrix = Matrix(dim=(self.row,self.col),value=0)
        
        if isinstance(other, Matrix):
            for i in range(self.row):    
                for j in range (self.col):
                    mul_matrix.M[i][j] = self.M[i][j] - other.M[i][j]
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(self.row):    
                for j in range (self.col):
                    mul_matrix.M[i][j] = self.M[i][j] * other
        return mul_matrix

    def __rmul__(self, other):
        return self.__mul__(other)

    
    def __getitem__(self,index):
        i ,j = index[0] , index[1]
        return self.M[i][j]
    def __setitem__(self,index,v):
        i ,j = index[0] , index[1]
        self.M[i][j] = v   


if __name__ == '__main__':
        # A=Matrix(dim=(3,4),value=2)
        # B=Matrix(dim=(3,3),value=3)
        D = Matrix(dim = (23, 2), value = [[-5.0, 1.0], [-4.795918367346939, 1.0], [-4.591836734693878, 1.0], [-3.979591836734694, 1.0], [-3.571428571428571, 1.0], [-2.9591836734693877, 1.0], [-2.7551020408163263, 1.0], [-1.7346938775510203, 1.0], [-1.3265306122448979, 1.0], [-0.9183673469387754, 1.0], [-0.7142857142857144, 1.0], [-0.3061224489795915, 1.0], [0.1020408163265305, 1.0], [0.7142857142857144, 1.0], [1.1224489795918373, 1.0], [1.7346938775510203, 1.0], [1.9387755102040813, 1.0], [2.5510204081632653, 1.0], [2.959183673469388, 1.0], [3.979591836734695, 1.0], [4.387755102040817, 1.0], [4.591836734693878, 1.0], [5.0, 1.0]])
        Z=D.transpose()@D
        print(Z)
        print(2 * Z)
        
        
    