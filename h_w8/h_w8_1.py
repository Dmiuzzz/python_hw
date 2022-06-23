class Date:
    d_m_y = []
    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def num_format(cls, param):
        num = 0
        count = 0

        for i in param:
            count += 1
            if i.isdigit() == True:
                num *= 10
                num += int(i)
                if count != len(param):
                    continue
            Date.d_m_y.append(num)
            num = 0
        return Date.d_m_y
    @staticmethod
    def valid_dt():
        if 1 > Date.d_m_y[0] or Date.d_m_y[0] > 31:
            return 'Error day'
        if 1 > Date.d_m_y[1] or Date.d_m_y[1] > 12:
            return 'Error month'
        if 1000 > Date.d_m_y[2] or Date.d_m_y[2] > 9999:
            return 'May bee Error "year"'
        return 'Date is ok'

print(Date.num_format(input("Input date xx.xx.xxxx ")))
print(Date.valid_dt())