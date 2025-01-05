import os
import random
from fuzzingbook.GrammarFuzzer import GrammarFuzzer

def generate_input(generated_roms_path):
    
    #  NES grammar
    EXPR_GRAMMAR: Grammar = {
    "<start>": ["<Header>"],  # Start symbol points to the 'Header' section
    "<Header>": ["NES", "<header_flags>", "<prg_size>", "<chr_size>", "<mapper_type>", "<mirroring_flags>"],
    "<header_flags>": ["<trainer_flag>", "<reserved>"],
    "<trainer_flag>": ["<trainer>"],  # Optional trainer section
    "<reserved>": ["<reserved_data>"],
    "<prg_size>": ["<prg_rom_banks>"],
    "<chr_size>": ["<chr_rom_banks>"],
    "<mapper_type>": ["<mapper_number>", "<extra_flags>"],
    "<mirroring_flags>": ["<mirroring>"],
    
    "<prg_rom_banks>": ["<prg_bank>"],
    "<chr_rom_banks>": ["<chr_bank>"],
    "<mapper_number>": ["<mapper_0>", "<mapper_1>", "<mapper_2>"],
    "<extra_flags>": ["<extra_flag>"],
    "<mirroring>": ["<vertical_mirroring>", "<horizontal_mirroring>"],
    
    "<prg_bank>": ["<prg_data>"],
    "<chr_bank>": ["<chr_data>"],
    
    "<prg_data>": ["<byte_data>"],
    "<chr_data>": ["<byte_data>"],
    
    "<byte_data>": ["<byte>"],  # Represents random byte data (could be anything)
    "<byte>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"],  # Represents any byte (0 to 255)
    
    "<reserved_data>": ["<zero_byte>"],  # Reserved data is usually zeroed out
    "<zero_byte>": ["0"],
    
    "<vertical_mirroring>": ["vertical"],
    "<horizontal_mirroring>": ["horizontal"],
    "<trainer>": ["<trainer_data>"],
    "<trainer_data>": ["<trainer_byte>"],  # 512 bytes trainer data
    "<trainer_byte>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"],
    
    "<mapper_0>": ["0"],
    "<mapper_1>": ["1"],
    "<mapper_2>": ["2"],
    "<extra_flag>": ["<flag>"],
    "<flag>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    }

    # Trim unused or unreachable rules from the grammar
    #EXPR_GRAMMAR = trim_grammar(EXPR_GRAMMAR)

    nes_grammar_f = GrammarFuzzer(EXPR_GRAMMAR)

    # Fuzz the grammar
    new_rom = nes_grammar_f.fuzz()

    # save to file
    file_name = generated_roms_path + f"/generated_{random.randint(0, 9999)}.nes"
    with open(file_name, "wb") as f:
        f.write(new_rom.encode())

    return file_name

