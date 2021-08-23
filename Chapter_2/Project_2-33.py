#!/usr/bin/env python
# coding: utf-8

# ## 2.33
# Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivate of that polynomial

# In[41]:


class TakeCoeffs:
    
    """This class take a plynomial in it's standard algebraic notation and capture its coefficients as a list
    
    Example::
            >> TakeCoeffs.coeffs("5*x^3 + 4*x^2 + 5*x + 1")
            >> [5, 4, 5, 1]
    
    This is class just with a class method and without constructor because the main purpose of this class is being 
    used within other class without needed of creatig a previus instance, this class has the same behavior than a function
    
    """
    @classmethod
    def coeffs(cls,pol):

        polynomialRegex = re.compile(r"(((-\s)?(-?\d+\*x|x|\d+))(\^-?\d+)?)")
        coeff_regex = re.compile(r"((-\s|-)?(\d+\*x|x|\d+))")
        group_coefficients = polynomialRegex.findall(pol)  
        group_coefficients = [mo[0].replace(" ", "") for mo in group_coefficients]
        all_coeffs = []
        for i in group_coefficients:
            if coeff_regex.search(i):
                coeff_mo = coeff_regex.search(i).group()
                if coeff_mo[0] == 'x' or coeff_mo[0:2] == '-x': 
                    coeff = 1
                    if coeff_mo[0] == '-':
                        coeff = -1
                else:
                    coeff = re.compile(r"-?\d+").search(coeff_mo).group() 
                all_coeffs.append(int(coeff))
                
        return all_coeffs 


# In[44]:


import re

class Polynomial:
    
    """ This class take a polynomial and return it's derivate, the input has to be given 
    either in standard algebraic notaion or with a list that represent their coefficients, also this class has
    a encapsulate behavior, then the constructor is void and it's parameter must be given with a setter
    
    Notes: - the polynomial must be written in a ordered way
           - the input must be passed with a setter 
    
    Attributes
    ----------
    
    _coeffs : list
        Contain a list with the coefficients of the polynomyal passed in
        
    _degrees : list
        Contain a list with the genereated degrees of the polynomial 
        
    Methods
    -------
    Coefficients:
        setter and getter of the polynomial's coefficients 
    
    Degrees:
        getter of the degrees of the polynomial
        
    PrintPoly(coeffs):
        take a list with the coefficients of a polynomial and return a ploynomial printed in standard algebraic notation
    
    Derivate():
        based on the coefficients generate a list eith the coefficients of it's derivate
        
    Example::  
    
            >> poly = Polynomial
            >> poly.Coefficients = [5,4,5,1] or  poly.Coefficients = "5*x^3 + 4*x^2 + 5*x + 1"
              
            >> print(poly)
            >> The Polynomial is: 5*x^3 + 4*x^2 + 5*x + 1, and it's derivate is: 15*x^2 + 8*x + 5*1
    
    """
    
    def __init__(self):
        """
        
        """
        self._polynomial = None
        self._coeffs = None
        self._degrees = None

    @property              # getter coefficients
    def Coefficients(self):
        return self._coeffs
    
    @Coefficients.setter   # setter coefficients 
    def Coefficients(self, coeffs):
        
        if isinstance(coeffs, str):      # here if the input is in algebraic notation
            self._coeffs = TakeCoeffs.coeffs(coeffs)
            self._degrees = [i-1 for i in range(len(TakeCoeffs.coeffs(coeffs)),1,-1)]
        else:
            self._coeffs = coeffs        # here if the input is a list
            self._degrees = [i-1 for i in range(len(coeffs),1,-1)]
        
    @property
    def Degrees(self):     # getter degrees the setter is no needed because are calculated
        return self._degrees
    
    def printPoly(self,coeffs):
        out = ''
        size = len(coeffs)  
        for d in range(size):        
            out += (str(coeffs[d]) + '*x^' + str(size - d - 1) + '+')
        out = out[:-1]        
        overallRegex = [r"\+-", r"x\^0", r"1\*", r"x\^1", r"\*1"] # list with regex to clean the out
        subs = ['-', '1', '', 'x', '']   # list with objects which will be repalce if overalregex match
        for e, expr in enumerate(overallRegex):
            polyRegex = re.compile(expr)
            out = polyRegex.sub(subs[e], out)             
        spaceRegex = re.compile(r"(\d|x)(\+|-)(\d|x)")          
        out = spaceRegex.sub(r"\1 \2 \3", out)
        return out
    
    def Derivate(self):  
        
        derivate_coeffs = []
        derivate_degrees = []       
        for i in range(len(self._degrees)):  # calculate the coeffs of the derivated polynomial
            derivate_coeffs.append(self._coeffs[i] * self._degrees[i])
        
        for i in self._degrees:   # calculate the degrees of the derivated polynomial
            derivate_degrees.append(i-1)
        
        return derivate_coeffs
    
    def __str__(self): 
        return (f'The Polynomial is: %s, and it\'s derivate is: %s'  % (self.printPoly(self._coeffs), 
                self.printPoly(self.Derivate())))


# ## Testing

# In[43]:



a = Polynomial()
a.Coefficients = [5,4,5,1]

b = Polynomial()
b.Coefficients = "5*x^3 + 4*x^2 + 5*x + 1"

a.Coefficients
b.Coefficients

print(a)

