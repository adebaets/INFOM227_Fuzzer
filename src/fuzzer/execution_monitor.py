import subprocess

def run_emulator(emulator_path, rom_file):
    try:
        result = subprocess.run([emulator_path, rom_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                timeout=5)
        if result.returncode != 0:
            with open("logs/crash_logs/crash_log.txt", "a") as log:
                log.write(f"ROM: {rom_file}\n")
                log.write(f"Stderr: {result.stderr.decode()}\n")
            print(f"Crash detected: {rom_file}")
        return result
    except subprocess.TimeoutExpired:
        print(f"Timeout occurred for ROM: {rom_file}")


