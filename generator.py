import random
import sys


def generar_instancia_subset_sum(nom_fitxer, num_elements=10, valor_maxim=50, forçar_solució=True):
    # Generem un conjunt de números aleatoris
    nums = [random.randint(1, valor_maxim) for _ in range(num_elements)]

    if forçar_solució:
        # Triem un subconjunt aleatori dels nums
        subconjunt = random.sample(nums, k=random.randint(1, len(nums)))
        target = sum(subconjunt)
    else:
        # Posem un target aleatori que potser no tingui solució
        target = random.randint(1, sum(nums))

    # Guardem al fitxer
    with open(nom_fitxer, 'w') as f:
        f.write(str(target) + '\n')
        for i in range(0, len(nums), 5):
            f.write(' '.join(map(str, nums[i:i+5])) + '\n')

    print(f"Instància guardada a '{nom_fitxer}' amb target = {target}")
    print(f"Números: {nums}")
    if forçar_solució:
        print(f"Subconjunt que suma {target}: {subconjunt}")

if __name__ == '__main__':
    num_elements = int(sys.argv[1])
    valor_maxim = int(sys.argv[2])
    generar_instancia_subset_sum("nums.txt", num_elements, valor_maxim)
