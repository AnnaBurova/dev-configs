#!/usr/bin/env bash
set +e  # continue on error

# > — Creates (or overwrites) the output.txt file.
# >> — Appends output to the end of an existing file.

cd "$(dirname "$0")" || exit 1

# === List of test modules ===
modules=("module1" "module2" "module3" "module4" "module5")


# === Loop each module ===
for mod in "${modules[@]}"; do
  echo "Running tests for: $mod"

  # base_path="D:/VS_Code/dev-project/tests/test_${mod}.py"

  # $ cd dev-project/tests/
  # $ ./_list.sh
  base_path="test_${mod}.py"

  for n in 1 2 3 4; do
    echo "tests/test_${mod} $n"
    case $n in
      1)
        pytest "$base_path" > "output/test_${mod}_${n}.txt"
        ;;
      2)
        pytest "$base_path" -v > "output/test_${mod}_${n}.txt" 2>&1
        ;;
      3)
        pytest "$base_path" -s > "output/test_${mod}_${n}.txt"
        ;;
      4)
        pytest "$base_path" -s -v > "output/test_${mod}_${n}.txt" 2>&1
        ;;
    esac
    # Convert to LF
    dos2unix --force "output/test_${mod}_${n}.txt"
  done
  echo "-----------------------------------------"
done

echo "✅ Done. Check output files (UTF-8 + LF)."
