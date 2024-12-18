from src.fuzzer.grammar_fuzzer import generate_input
from src.fuzzer.mutation_fuzzer import mutate_rom
from src.fuzzer.execution_monitor import run_emulator

def main():
    emulator_path = "./src/emulator/idk"  # need to add the emul!!!!
    valid_rom_path = "./test_cases/original_roms/valid_rom.nes"  # faut trouver des files valides!!

    # Grammar-based generation
    for _ in range(5):
        print("Generating new ROM...")
        new_rom = generate_input()
        run_emulator(emulator_path, new_rom)

    # Mutation-based testing
    for _ in range(5):
        print("Mutating ROM...")
        mutated_rom = mutate_rom(valid_rom_path)
        run_emulator(emulator_path, mutated_rom)

if __name__ == "__main__":
    main()
