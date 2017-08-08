class DecBin:
    NO_BITS = ''    #This determine how many bits to use to calculate the Binary fraction
    intpart =''
    floatpart = ''
    digitlenght = ''
    base = ''
    finalbinarypart = ''
    finalinteger = ''

    def __init__(self, fracNumber, base=2, bits=32):
        """This class convert Decimal number (base 10 to any Binary number"""
        DecBin.NO_BITS = bits
        DecBin.base = base
        self.getNUmber(fracNumber)

    def getNUmber(self,fracNumber):
        '''This check for a valid Fraction number'''
        fracNumber = str(fracNumber)
        self.__isvalidFraction(fracNumber)

    def __isvalidFraction(self,fracNumber):
        try:
            self.intpart, self.floatpart = fracNumber.split('.')
            self.digitstripper(self.floatpart)
            self.intDec2Bin(self.intpart)
        except ValueError:
            print('Enter Decimal Number')

        self.finalOutput(DecBin.finalinteger, DecBin.finalbinarypart)

    def digitstripper(self, floatpart):
        '''This is use to extract the leading digit when one is determine binary equivalent of fraction part '''
        if len(floatpart) < int(DecBin.NO_BITS):pass
        else:
            floatpart = floatp[:DecBin.NO_BITS]
        self.__floatlenght__(floatpart)
        self.floatDec2Bin(floatpart)

    def __floatlenght__(self, floatpart):
        digitlenght = len(floatpart)
        DecBin.digitlenght = digitlenght

    def floatDec2Bin(self, floatpart):
        '''This convert Fraction part of the given number to its equivalent Binary number,
        The precision is based on NO_BITS declared when the class is called, default precisoin is 32
        '''
        count = 0
        BinaryPart = []
        self.floatpart = floatpart
        digitlenght = int(DecBin.digitlenght)
        self.pre_floatpart = ''
        while count <= int(DecBin.NO_BITS):
            if count != 0:
                if len(self.pre_floatpart) > digitlenght:
                    currentfloatpart = str(int(self.pre_floatpart[1:]) * int(DecBin.base))
                else:currentfloatpart = str(int(self.pre_floatpart) * int(DecBin.base))
                k = currentfloatpart
                if k[0] != str(1):
                    BinaryPart.append('0')
                else:
                    BinaryPart.append(k[0])
                self.pre_floatpart = k
            else:
                k = int(self.floatpart)*2
                k = str(k)
                if k[0] != str(1):
                    BinaryPart.append('0')
                else:
                    BinaryPart.append(k[0])
                self.pre_floatpart = k
            count +=1
            DecBin.finalbinarypart  = self.list2string(BinaryPart)

    def intDec2Bin(self,intpart):
        '''This convert Integer part to its equivalent Binary Number'''
        count = 0
        IntPartList = []
        self.intpart = intpart
        while count <= int(DecBin.NO_BITS):
            if self.intpart == str(1):
                IntPartList.append(str(intpart))
            else:
                IntPartList.append(str(int(self.intpart) % int(DecBin.base)))
                quotient = int(self.intpart) // int(DecBin.base)
                self.intpart = quotient
            count +=1
        DecBin.finalinteger = self.list2string(IntPartList)

    def trailZeroStripper(self,stringwithleadingzero):
        '''This strip all the leading ZEROS in the interger part of the result'''
        leadingOnepos = stringwithleadingzero.find('1')
        return (stringwithleadingzero[leadingOnepos:])

    def list2string(self, listobject):
        '''List Object is converted to String object, and String object is return '''
        stringobj = ''.join(listobject)
        stringobj =self.StringReverser(stringobj)
        strobj = self.trailZeroStripper(stringobj)
        return (strobj)

    def StringReverser(self,string):
        '''This method reverse any given string
        This is use to reverse the binary result for the integer part
        '''
        return (string[::-1])

    def finalOutput(self,finalintegers, finalbinary):
        print(DecBin.finalinteger +'.'+ DecBin.finalbinarypart)


DecBin(100.6788,bits=16)    # when you wishes to specify lenght of the resulting fraction
DecBin(99.077)                # for now use float number to get accurate result
