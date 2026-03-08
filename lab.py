A = [1, 2, 3]
B = [3, 4, 5]

sym_diff = [x for x in A if x not in B] + [x for x in B if x not in A]
cartesian_prod = [(a, b) for a in A for b in B]

print("Симетрична різниця:", sym_diff)
print("Декартовий добуток:", cartesian_prod)