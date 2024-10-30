class Flipkart:
    products={'shoe':600,'smwatch':500,'mobile':14000}
    def _init_(self,name,accno,bal):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.store=[]
    def display(self):
        print(self.name,self.accno,self.bal,self.store)

    def debit(self,amt):
        if amt<self.bal:
            self.bal=self.bal-amt
            print('amount debited successfully')
        else:
            print('insufficient balance')
    def product(self,price):
        prod_name=input('enter:')
        self.products[prod_name]=price




    def buy(self,paytype):
        prod_name=input('enter product name:')
        if prod_name in Flipkart.products:
            price=self.products[prod_name]
            pay=input('enter type of payment:')
            if paytype=='cod':
                print(f'{prod_name}is ordered successfully')
                

            
            elif paytype=='upi':
                self.bal=self.debit(amt)
                print(f'order for {prod_name} is placed of {price} successfully')

            elif paytype=='debitcard':
                num=int(input('enter card number:'))
                import random
                genotp=random.randint(1000,9999)
                print('otp for debit card is{otp}')
               #otp=int(input('enter otp'))

                if genotp==int(input('enter otp:')):
                    print('otp verified')
                    self.bal=self.debit(price)
                    print('successfully debited amount')
            else:
                print('invalid paytype ')
                
        else:
            print('product not available')
ran=Flipkart('ranga',12783632,50000)
ran.display()