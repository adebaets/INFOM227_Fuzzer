from src.fuzzer.grammar_fuzzer import generate_input
from src.fuzzer.mutation_fuzzer import mutate_rom
from src.fuzzer.execution_monitor import run_emulator
import argparse

# command line setup
def parse_args():
    parser = argparse.ArgumentParser(description="Fuzz NES Emulator with Grammar-based and Mutation-based testing")
    parser.add_argument("emulator_path", help="Path to the emulator binary")
    parser.add_argument("--valid_rom_path", default="./test_cases/original_roms/valid_rom.nes", help="Path to a valid ROM for mutation")
    parser.add_argument("--generated_roms_path", default="./test_cases/generated_roms/", help="Path to save generated ROMs")
    parser.add_argument("--mutated_roms_path", default="./test_cases/mutated_roms/", help="Path to save mutated ROMs")
    parser.add_argument("--num_tests", type=int, default=5, help="Number of tests to run for both generation and mutation")

    return parser.parse_args()


def main():
    args = parse_args()

    emulator_path = args.emulator_path
    valid_rom_path = args.valid_rom_path
    generated_roms_path = args.generated_roms_path
    mutated_roms_path = args.mutated_roms_path
    num_tests = args.num_tests


    # Grammar-based generation
    for _ in range(num_tests):
        print("Generating new ROM...")
        new_rom = generate_input(generated_roms_path)
        run_emulator(emulator_path, new_rom)

    # Mutation-based testing
    for _ in range(num_tests):
        print("Mutating ROM...")
        mutated_rom = mutate_rom(valid_rom_path, mutated_roms_path)
        run_emulator(emulator_path, mutated_rom)


if __name__ == "__main__":
    main()

