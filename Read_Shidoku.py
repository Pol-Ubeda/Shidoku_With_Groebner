import sympy as sp
from sympy import symbols,groebner
import json

class Shidoku():
    def read_data(self,shidoku_file):
        with open(shidoku_file,'r') as json_file:
            data=json.load(json_file)
        return data
    
    def polys(self):
        polynomials1=[]
        polynomials2=[]
        data=self.read_data('shidoku_numbers.json')
        variables=symbols('x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15')

        for i in range(4):
            polynomials2.append(variables[i*4+0]+variables[i*4+1]+variables[i*4+2]+variables[i*4+3]-10)
            polynomials2.append(variables[i*4+0]*variables[i*4+1]*variables[i*4+2]*variables[i*4+3]-24)


            for j in range(4):
                if data['shidoku'][i][j] is not None:
                    polynomials1.append(variables[i*4+j]-data['shidoku'][i][j])
                else:
                    polynomials2.append((variables[i*4+j]-4)*(variables[i*4+j]-1)*(variables[i*4+j]-2)*(variables[i*4+j]-3))
                if i==0:
                    polynomials2.append(variables[j]+variables[4+j]+variables[4*2+j]+variables[4*3+j]-10)
                    polynomials2.append(variables[j]*variables[4+j]*variables[4*2+j]*variables[4*3+j]-24)
                    
        
        polynomials2.append(variables[0]+variables[1]+variables[4*1]+variables[4*1+1]-10)
        polynomials2.append(variables[0]*variables[1]*variables[4*1]*variables[4*1+1]-24)

        polynomials2.append(variables[2]+variables[3]+variables[4*1+2]+variables[4*1+3]-10)
        polynomials2.append(variables[2]*variables[3]*variables[4*1+2]*variables[4*1+3]-24)

        polynomials2.append(variables[4*2]+variables[4*2+1]+variables[4*3]+variables[4*3+1]-10)
        polynomials2.append(variables[4*2]*variables[4*2+1]*variables[4*3]*variables[4*3+1]-24)

        polynomials2.append(variables[4*2+2]+variables[4*2+3]+variables[4*3+2]+variables[4*3+3]-10)
        polynomials2.append(variables[4*2+2]*variables[4*2+3]*variables[4*3+2]*variables[4*3+3]-24)

        polynomials=polynomials1+polynomials2
        return polynomials

        
             
         
    
test=Shidoku()
polynomials=test.polys()
variables=symbols('x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15')

groebner_basis=list(sp.groebner(polynomials,variables, order='grlex'))
print(groebner_basis)