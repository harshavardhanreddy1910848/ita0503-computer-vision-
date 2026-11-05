import os
import subprocess
import glob
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROG_DIR = os.path.join(BASE_DIR, 'programs')
OUT_DIR = os.path.join(BASE_DIR, 'output_screenshots')

program_files = sorted(glob.glob(os.path.join(PROG_DIR, 'exp*.py')))
print(f"Found {len(program_files)} programs to execute.")

success_count = 0
failed = []

for pf in program_files:
    prog_name = os.path.basename(pf)
    print(f"Running {prog_name}...", end=" ")
    sys.stdout.flush()
    try:
        res = subprocess.run([sys.executable, pf], cwd=PROG_DIR, capture_output=True, text=True, timeout=30)
        if res.returncode == 0:
            print("OK")
            success_count += 1
        else:
            print("ERROR:")
            print(res.stderr[:200])
            failed.append((prog_name, res.stderr))
    except Exception as e:
        print("EXCEPTION:", e)
        failed.append((prog_name, str(e)))

print(f"\nExecution Complete: {success_count}/{len(program_files)} succeeded.")
if failed:
    print(f"Failed programs: {[f[0] for f in failed]}")

out_files = glob.glob(os.path.join(OUT_DIR, '*.png'))
print(f"Total output screenshots in '{OUT_DIR}': {len(out_files)}")

