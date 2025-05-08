import time
import random
import string
from algorithms import shiftCipher, affineCipher, vigenereCipher

# Define test sizes and rounds
TEXT_LENGTHS = [50, 100, 500, 1000, 2000, 5000]
ROUNDS_PER_TEST = 5  # 每个长度测试5轮取平均

# Define keys
SHIFT_KEY = 5
AFFINE_KEY_A, AFFINE_KEY_B = 5, 8
VIGENERE_KEY = "KEY"

ENGLISH_CORPUS = """
It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.
""".replace('\n', ' ').upper()

# Function to generate random plaintext
def generate_random_text(length):
    # Repeat the corpus if needed
    full_text = (ENGLISH_CORPUS * ((length // len(ENGLISH_CORPUS)) + 1))[:length]
    # Remove non-alphabetic characters and keep only letters
    return full_text

# Store results
results = []

for length in TEXT_LENGTHS:
    print(f"\n=== Testing with plaintext length: {length} (Averaging over {ROUNDS_PER_TEST} rounds) ===")
    
    shift_times = []
    affine_times = []
    vigenere_times = []

    for round_num in range(ROUNDS_PER_TEST):
        plaintext = generate_random_text(length)

        # --- Shift Cipher Test ---
        cipher_shift = shiftCipher.shiftEnc(plaintext, SHIFT_KEY)
        start = time.perf_counter()
        _ = shiftCipher.shiftAnalysis(cipher_shift)
        end = time.perf_counter()
        shift_times.append(end - start)
        
        # --- Affine Cipher Test ---
        cipher_affine = affineCipher.affineEnc(plaintext, AFFINE_KEY_A, AFFINE_KEY_B)
        start = time.perf_counter()
        _ = affineCipher.affineAnalysis(cipher_affine)
        end = time.perf_counter()
        affine_times.append(end - start)
        
        # --- Vigenère Cipher Test ---
        cipher_vigenere = vigenereCipher.vigEnc(plaintext, VIGENERE_KEY)
        start = time.perf_counter()
        _ = vigenereCipher.vigAnalysis(cipher_vigenere)
        end = time.perf_counter()
        vigenere_times.append(end - start)

        print(f"  Round {round_num + 1}: Shift={shift_times[-1]:.4f}s, Affine={affine_times[-1]:.4f}s, Vigenere={vigenere_times[-1]:.4f}s")

    avg_shift = sum(shift_times) / ROUNDS_PER_TEST
    avg_affine = sum(affine_times) / ROUNDS_PER_TEST
    avg_vigenere = sum(vigenere_times) / ROUNDS_PER_TEST

    print(f"Average: Shift={avg_shift:.4f}s, Affine={avg_affine:.4f}s, Vigenere={avg_vigenere:.4f}s")

    results.append({
        "Length": length,
        "Shift_Avg": avg_shift,
        "Affine_Avg": avg_affine,
        "Vigenere_Avg": avg_vigenere
    })

# Print summary table
print("\n=== Performance Summary (Averaged) ===")
print(f"{'Length':<10} {'Shift(s)':<12} {'Affine(s)':<12} {'Vigenere(s)':<12}")
for r in results:
    print(f"{r['Length']:<10} {r['Shift_Avg']:<12.5f} {r['Affine_Avg']:<12.5f} {r['Vigenere_Avg']:<12.5f}")
