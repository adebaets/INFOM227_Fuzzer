import os
import random
from fuzzingbook.Grammars import Grammar, fuzz_grammar

def generate_input(generated_roms_path):
    #  NES grammar
    nes_grammar = Grammar.from_pattern({
        'header': 'NES\x1A',  # NES 4 magic bytes
        'prg_size': ['1', '2', '4'],  # PRG-ROM size in 16KB units
        'chr_size': ['0', '1', '2'],  # CHR-ROM size in 8KB units
        'flags': random.randint(0, 255).to_bytes(2, byteorder="little"),  # Random flags
        'padding': b"\x00" * 8,  # Padding
        'prg_data': os.urandom(random.choice([1, 2, 4]) * 16 * 1024),  # PRG data
        'chr_data': os.urandom(random.choice([0, 1, 2]) * 8 * 1024),  # CHR data
    })

    # Fuzz the grammar
    new_rom = fuzz_grammar(nes_grammar)

    # save to file
    file_name = generated_roms_path + f"/generated_{random.randint(0, 9999)}.nes"
    with open(file_name, "wb") as f:
        f.write(new_rom)

    return file_name

