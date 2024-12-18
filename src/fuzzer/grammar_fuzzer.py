import os
import random

def generate_input():
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
