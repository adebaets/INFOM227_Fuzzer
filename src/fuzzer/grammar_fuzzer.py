import os
import random
from fuzzingbook.Grammars import Grammar, fuzz_grammar

def generate_input():
    # Define a simple grammar for the NES ROM structure
    nes_grammar = Grammar.from_pattern({
        'header': 'NES\x1A',  # NES magic bytes
        'prg_size': ['1', '2', '4'],  # PRG-ROM size in 16KB units
        'chr_size': ['0', '1', '2'],  # CHR-ROM size in 8KB units
        'flags': lambda: random.randint(0, 255).to_bytes(2, byteorder="little"),  # Random flags
        'padding': lambda: b"\x00" * 8,  # Padding
        'prg_data': lambda: os.urandom(random.choice([1, 2, 4]) * 16 * 1024),  # PRG data
        'chr_data': lambda: os.urandom(random.choice([0, 1, 2]) * 8 * 1024),  # CHR data
    })

    # Fuzz the grammar to create a new NES ROM
    new_rom = fuzz_grammar(nes_grammar)

    # Save the ROM to file
    file_name = f"./test_cases/generated_roms/generated_{random.randint(0, 9999)}.nes"
    with open(file_name, "wb") as f:
        f.write(new_rom)

    return file_name


def generate_input2():
    # iNES header grammar
    header = b"NES\x1A"  # NES 4 first bytes
    prg_size = random.choice([1, 2, 4])  # PRG-ROM size in 16KB units
    chr_size = random.choice([0, 1, 2])  # CHR-ROM size in 8KB units
    flags = random.randint(0, 255).to_bytes(2, byteorder="little")  # Flags
    padding = b"\x00" * 8

    # PRG and CHR data
    prg_data = os.urandom(prg_size * 16 * 1024)
    chr_data = os.urandom(chr_size * 8 * 1024)

    # Combine everything into a ROM
    rom = header + bytes([prg_size, chr_size]) + flags + padding + prg_data + chr_data

    # Save to file
    file_name = f"./test_cases/generated_roms/generated_{random.randint(0, 9999)}.nes"
    with open(file_name, "wb") as f:
        f.write(rom)

    return file_name



