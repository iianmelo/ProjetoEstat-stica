import random

###DrugA == 0
###DrugB == 1
###DrugC == 2
###DrugX == 3
###DrugY == 4

## F = 0
## M = 1

## Blood Pressure High = 1
## Blood Pressure Normal = 2
## Blood Pressure Low = 3

## Cholesterol High = 1
## Cholesterol Normal = 2
## Cholesterol Low = 3

# Função para aumentar o banco de dados gerando amostras pseudo-aleatórias
def generate_samples(num_samples):
    samples = []

    for _ in range(num_samples):
        age = random.randint(20, 80)
        sex = random.choice([1, 0])
        if age < 50:
            bp = random.choice([1, 2])
            if bp == 1:
                cholesterol = random.choice([1, 2, 3])
                if cholesterol == 1:
                    na_to_k = round(random.uniform(6, 30), 3)
                    drug = 0 if random.random() < 0.5 else 3
                elif cholesterol == 2:
                    na_to_k = round(random.uniform(3, 6), 3)
                    drug = 3
                else:
                    na_to_k = round(random.uniform(2, 3), 3)
                    drug = 3
            else:
                cholesterol = random.choice([2, 3])
                if cholesterol == 2:
                    na_to_k = round(random.uniform(2, 5), 3)
                    drug = 3
                else:
                    na_to_k = round(random.uniform(1, 2), 3)
                    drug = 3
        else:
            bp = random.choice([1, 2, 3])
            if bp == 1:
                cholesterol = random.choice([1, 2, 3])
                if cholesterol == 1:
                    na_to_k = round(random.uniform(6, 30), 3)
                    drug = 1 if random.random() < 0.5 else 4
                elif cholesterol == 2:
                    na_to_k = round(random.uniform(3, 6), 3)
                    drug = 4
                else:
                    na_to_k = round(random.uniform(2, 3), 3)
                    drug = 4
            elif bp == 2:
                cholesterol = random.choice([2, 3])
                if cholesterol == 2:
                    na_to_k = round(random.uniform(2, 5), 3)
                    drug = 4
                else:
                    na_to_k = round(random.uniform(1, 2), 3)
                    drug = 4
            else:
                cholesterol = random.choice([2, 3])
                if cholesterol == 2:
                    na_to_k = round(random.uniform(1, 3), 3)
                    drug = 2
                else:
                    na_to_k = round(random.uniform(0.5, 1), 3)
                    drug = 2

        samples.append([age, sex, bp, cholesterol, na_to_k, drug])

    return samples

# Gerando 10.000 amostras
samples = generate_samples(10000)

# Escrevendo as amostras em um arquivo CSV
with open('drug_samples.csv', 'w') as file:
    file.write("Age,Sex,BP,Cholesterol,Na_to_K,Drug\n")
    for sample in samples:
        file.write(','.join(map(str, sample)) + '\n')

print("Amostras geradas e salvas em drug_samples.csv.")
