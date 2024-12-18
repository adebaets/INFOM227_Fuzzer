import random

def mutate_rom(input_file):
    with open(input_file, "rb") as f:
        data = bytearray(f.read())

    # random mutations
    mutation_count = random.randint(1, 10)
    for _ in range(mutation_count):
        index = random.randint(0, len(data) - 1)
        data[index] = random.randint(0, 255)

    # save
    output_file = input_file.replace("original_roms", "mutated_roms").replace(".nes", "_mutated.nes")
    with open(output_file, "wb") as f:
        f.write(data)

    return output_file
