print("hello")
def CompoundInterestCalculator(savings, annualInterestRate, years ):
    
    multiply = annualInterestRate/100
    for i in range (years):
        savings *= 1 + multiply
        text1 = "Your savings after " + str(i+1) + " years is " + str(savings)
        print(text1)
    number_of_years_to_double = 72/multiply

    text = "Your savings after " + str(years) + " years is " + str(savings) +". Your savings will double in " + str(number_of_years_to_double)
    return text

print(CompoundInterestCalculator(1000, 50, 10))