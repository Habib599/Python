class calculator:
    brand = 'Casio MS990'
    
    def add(self, num1, num2):
        print( num1 + num2)

    def subtract(self, num1, num2):
        print( num1 - num2)

    def multiply(self, num1, num2):
        print( num1 * num2)

    def divide(self, num1, num2):
        
        print( num1 / num2)


c=calculator()

c.add(3,9)
c.subtract(9,4)
c.multiply(4,8)
c.divide(8,4)