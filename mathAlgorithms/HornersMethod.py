def horner( polynomialsFactors, polynominalDegree, x ):
    result = polynomialsFactors[0]

    for i in range(1, polynominalDegree+1):
        result = result*x + polynomialsFactors[i]

    return result

factors = [1,-3,5,-15]
degree = 3
rest = horner(factors,degree,3)
print(rest)

factors = [5,0,0,6,-3]
degree = 4
rest = horner(factors,degree,-1)
print(rest)