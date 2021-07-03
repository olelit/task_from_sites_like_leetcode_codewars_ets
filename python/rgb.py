def format(val):
    if val < 0: val = 0
    if val > 255: val = 255
    output = '{:02X}'.format(val)
    return output


def rgb(r, g, b):
    rgb = (r, g, b)
    hex_result = "".join([format(val) for val in rgb])
    return hex_result

print(max(0,min(2,5)))
print(rgb(1,2,3))
