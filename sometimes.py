def sometimes(val):
    limit = 10
    import random
    x = random.random()*100
    mag = 100.0
    a = mag*(val+x)/ x
#    a = int(str(a)[:str(a).find('.')])/mag - 1
    a = round(a, 2)/mag-1
    b = mag*(limit+x)/x
#   b = b/mag - 1
    b = round(b, 2)/mag-1
#    b = int(str(b)[:str(b).find('.')])/mag - 1
    val = a/b*limit
    return val
    
def run(value):
    value = sometimes(value)
    print value
    return run(value)
	

value = eval(raw_input())
ref = value
i ,more,less,equal= 0,0,0,0
while i<10000000:
    value = sometimes(value)
    if value> ref:more+=1
    elif value< ref:less+=1
    elif value ==ref:equal+=1
    i = i + 1
    print value, 'more',more,'equal',equal,'less',less

