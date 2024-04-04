import time

class Reader:
    lines = list()
    data = list()
    
    def __init__(self) -> None:
        pass
    
    def read_text(self,path):
        with open(path, 'r') as file:
            content = file.readlines()
            content = list(content)
            self.lines = [list(line) for line in content]
            self.data = [[ord(char) for char in line] for line in self.lines]


class Linear_math:
    def __init__(self) -> None:
        pass
    def mcd(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def linear_congruence(self,a, b, m):
        if b == 0:
            return 0
        if a < 0:
            a = -a
            b = -b
        b %= m
        while a > m:
            a -= m
        return (m * self.linear_congruence(m, -b, a) + b) // a

class Criptography:
    p = 11
    q = 31
    euler_function = (p - 1)*(q -1)
    math = Linear_math()
    n = p * q
    
    e = 0
    d = 0
    
    msg = list()
    
    def __init__(self) -> None:
        pass

class Encoder(Criptography):
    def find_d(self):
        d = 2
        nums = list()
        for d in range(2,self.euler_function):
            num = self.math.mcd(d,self.euler_function)
            if num == 1:
                #print(d,self.euler_function,num)
                nums.append(d)
        print(nums)
        return nums[0]    
    def get_keys(self):
        self.d = self.find_d()
        self.private_key = [self.n,self.d]
        
        #dE === 1 mod phi
        #aX ≡ b (mod m)
        
        self.e = self.math.linear_congruence(self.d,1,self.euler_function)
        print(self.n,self.e)
        print('private:',self.n,self.d)
        print('public:',self.n,self.e)
        
    def encode(self):
        
        encripted_data = [[chr((pow(line,self.e))%self.n) for line in lines] for lines in self.msg]
        print(encripted_data)
        desencripted_data = [[chr((pow(ord(line),self.d))%self.n) for line in lines] 
                            for lines in encripted_data] #list comprenhension
        print(desencripted_data)



if __name__ == '__main__':
    tiempo_inicio = time.time()
    
    lector = Reader()
    lector.read_text('proyecto3mate/mensaje.txt')
    print(lector.lines[7])
    print(lector.data[7])
    
    emisor = Encoder()
    emisor.msg = lector.data
    #print(emisor.msg)
    
    emisor.get_keys()
    emisor.encode()
    
    tiempo_final = time.time()
    print('\n\nTIEMPO TOTAL:' , (tiempo_final - tiempo_inicio)*100 , 'ms')