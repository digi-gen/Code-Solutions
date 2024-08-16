# https://quera.org/problemset/6404

class Reaction:

    def __init__(self, pre_materials: set, response_materials: set):
        self.pre_materials = pre_materials
        self.response_materials = response_materials


reactions = []

n, m, k = map(int, input().split())
owned_materials = {a: False for a in range(1, n+1)}
for i in map(int, input().split()):
    owned_materials[i] = True

for i in range(k):
    pre_n, response_n = map(int, input().split())
    pre_materials = set(map(int, input().split()))
    response_materials = set(map(int, input().split()))

    reactions.append(Reaction(pre_materials, response_materials))


while True:

    for i in range(len(reactions)):
        pre_materials_i = reactions[i].pre_materials
        if all(((owned_materials[pre_mat]) for pre_mat in pre_materials_i)):
            for response_mat in reactions[i].response_materials:
                owned_materials[response_mat] = True
            reactions.pop(i)
            break
    else:
        break


# print results
owned_materials = [key for key in owned_materials.keys() if owned_materials[key]]
print(len(owned_materials))
owned_materials = sorted(owned_materials)
print(*owned_materials, end=' ')
