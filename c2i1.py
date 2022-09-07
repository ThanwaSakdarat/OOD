class translator:

    def deciToRoman(self, num):
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
        i = 12  
        roman_numeral = ''
        while num != 0:
            if numbers[i] <= num:    
                roman_numeral += roman[i] 
                num = num - numbers[i]
            else:
                i -= 1 
        return roman_numeral 

    def romanToDeci(self, num):
        print(num)

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(num)