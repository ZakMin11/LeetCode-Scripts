class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if str(dividend)[0] == '-' and str(divisor)[0] == '-':
            divisor = int(str(divisor)[1:])
            dividend = int(str(dividend)[1:])
            return int(str((dividend//divisor)).split('.')[0])
        if str(dividend)[0] == '-':
            dividend = int(str(dividend)[1:])
            return int('-'+str((dividend//divisor)).split('.')[0])
        if str(divisor)[0] == '-':
            divisor = int(str(divisor)[1:])
            return int('-'+str((dividend//divisor)).split('.')[0])

        return int(str((dividend//divisor)).split('.')[0])

    d1=10
    dd1 =3
    d2 = 7
    dd2 = -3
    d3 = -1
    dd3 = -1
    print(divide(0,d1,dd1))
    print(divide(0,d2,dd2))
    print(divide(0,d3,dd3))
