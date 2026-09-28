#Write program to find compound interest using assignment operator.IMP QUESTION.
# principle=10000 ,Rate=10%,Time=2 years.



Principle=10000
rate=10
Time=2 
amount=Principle
for i in range(Time):
 interest=amount*rate/100
 amount+=interest
print("Amount :",amount)
print("Compound interest :",amount-Principle)
