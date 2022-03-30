'''
lec9 class
'''

class car:
    maker = 'toyota'
    
    def __init__(self,input_model):
        self.model=input_model
        
my_corolla = car('corolla')
my_highlander = car('highlander')

print(my_corolla.maker, my_corolla.model)

print(my_highlander.maker, my_highlander.model)