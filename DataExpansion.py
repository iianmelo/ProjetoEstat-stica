import random

# Função para aumentar o banco de dados gerando amostras pseudo-aleatórias
def generate_samples(num_samples):
    samples = []

    for _ in range(num_samples):
        age = random.randint(20, 80)
        sex = random.choice(['M', 'F'])
        if age < 50:
            bp = random.choice(['HIGH', 'NORMAL'])
            if bp == 'HIGH':
                cholesterol = random.choice(['HIGH', 'NORMAL', 'LOW'])
                if cholesterol == 'HIGH':
                    na_to_k = round(random.uniform(6, 30), 3)
                    drug = 'DrugA' if random.random() < 0.5 else 'DrugX'
                elif cholesterol == 'NORMAL':
                    na_to_k = round(random.uniform(3, 6), 3)
                    drug = 'DrugX'
                else:
                    na_to_k = round(random.uniform(2, 3), 3)
                    drug = 'DrugX'
            else:
                cholesterol = random.choice(['NORMAL', 'LOW'])
                if cholesterol == 'NORMAL':
                    na_to_k = round(random.uniform(2, 5), 3)
                    drug = 'DrugX'
                else:
                    na_to_k = round(random.uniform(1, 2), 3)
                    drug = 'DrugX'
        else:
            bp = random.choice(['HIGH', 'NORMAL', 'LOW'])
            if bp == 'HIGH':
                cholesterol = random.choice(['HIGH', 'NORMAL', 'LOW'])
                if cholesterol == 'HIGH':
                    na_to_k = round(random.uniform(6, 30), 3)
                    drug = 'DrugB' if random.random() < 0.5 else 'DrugY'
                elif cholesterol == 'NORMAL':
                    na_to_k = round(random.uniform(3, 6), 3)
                    drug = 'DrugY'
                else:
                    na_to_k = round(random.uniform(2, 3), 3)
                    drug = 'DrugY'
            elif bp == 'NORMAL':
                cholesterol = random.choice(['NORMAL', 'LOW'])
                if cholesterol == 'NORMAL':
                    na_to_k = round(random.uniform(2, 5), 3)
                    drug = 'DrugY'
                else:
                    na_to_k = round(random.uniform(1, 2), 3)
                    drug = 'DrugY'
            else:
                cholesterol = random.choice(['NORMAL', 'LOW'])
                if cholesterol == 'NORMAL':
                    na_to_k = round(random.uniform(1, 3), 3)
                    drug = 'DrugC'
                else:
                    na_to_k = round(random.uniform(0.5, 1), 3)
                    drug = 'DrugC'

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
