def ternary_out(x, min_digits):
    i = 0
    l = []
    while x > 0 or i < min_digits:
        l.append(x % 3)
        x //= 3
        i += 1
    return l

if input == "":
    n = 1
    queue = []
    while len(queue) < 1000:
        n = (n + 31) % 243
        #Exploits my 1(loop'd)D Knight's Tour theorem to generate
        #a nonrepeating sequence of sequences of moves.
        #(31 and 243 are relatively prime; (log_3 243) * 243 > 1000)
        queue.extend(ternary_out(n, 5))

output = queue.pop(0)
if output == 0:
    output = "R"
elif output == 1:
    output = "P"
else:
    output = "S"