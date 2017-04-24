lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVQXYZ'
nums = '0123456789'

def min(passw):
    ret = [0 if x in lower else 1 if x in upper else 2 if x in nums else 3 for x in passw]
    return 0 in ret and 1 in ret and 2 in ret

def strength(passw):
    ret = 0
    stren = [0 if x in lower else 1 if x in upper else 2 if x in nums else 3 for x in passw]
    #5 criteria, 2 points each
    if 0 in stren:
        ret += 2
    if 1 in stren:
        ret += 2
    if 2 in stren:
        ret += 2
    #special chars
    if 3 in stren:
        ret += 2
    if len(passw) > 5:
        ret += 2
    if len(passw) > 10:
        ret += 2
    return ret

print min('Pass123')
print min('pass123')
print min('')
print min('pass')
print min('Pass')
print min('P1')

print strength('Pass12345')
print strength('pass123')
print strength('12')
print strength('passssssssssssss')
print strength(" ")
