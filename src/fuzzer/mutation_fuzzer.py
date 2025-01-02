from fuzzingbook.Mutators import RandomMutator
def mutate_rom(input_file, mutated_roms_path):
    with open(input_file, "rb") as f:
        data = bytearray(f.read())

    # mutation
    mutator = RandomMutator()
    mutated_data = mutator.mutate(data)

    # Save
    output_file = mutated_roms_path + os.path.basename(os.path.normpath(input_file)).replace("original_roms", "mutated_roms").replace(".nes", "_mutated.nes")
    with open(output_file, "wb") as f:
        f.write(mutated_data)

    return output_file