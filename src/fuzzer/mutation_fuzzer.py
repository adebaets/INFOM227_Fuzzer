from fuzzingbook.Mutators import RandomMutator
def mutate_rom(input_file):
    with open(input_file, "rb") as f:
        data = bytearray(f.read())

    # Use fuzzingbook's RandomMutator for mutation
    mutator = RandomMutator()
    mutated_data = mutator.mutate(data)

    # Save mutated ROM
    output_file = input_file.replace("original_roms", "mutated_roms").replace(".nes", "_mutated.nes")
    with open(output_file, "wb") as f:
        f.write(mutated_data)

    return output_file