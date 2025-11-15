
def Integer_to_Roman(Integer):
    Roman = ''
    if not (0 < Integer < 4000):
        return "Input must be between 1 and 3999"
    Integer = str(Integer)[::-1]
    for i in range(len(str(Integer))):
        if i == 0:
            Ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
            Roman = Ones[int(Integer[i])] + Roman
        elif i == 1:
            Tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
            Roman = Tens[int(Integer[i])] + Roman
        elif i == 2:
            Hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
            Roman = Hundreds[int(Integer[i])] + Roman
        elif i == 3:
            Thousands = ['','M','MM','MMM']
            Roman = Thousands[int(Integer[i])] + Roman
        
    return Roman

print(Integer_to_Roman(3999))