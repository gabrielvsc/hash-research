import time
import hashlib
import bcrypt
import argon2
from tqdm import tqdm
from generators.hash_generator import generate_hashes
from attacks.brute_force import brute_force_attack

def main():
    test_password = "password123"
    hashes = generate_hashes(test_password)
    
    with open("data/rockyou.txt", "r", encoding="latin-1") as f:
        wordlist = f.readlines()
    
    results = {}
    for hash_type, hash_value in hashes.items():
        if hash_type in ["MD5", "SHA-1", "SHA-256"]:
            time_taken = brute_force_attack(hash_value, hash_type, wordlist)
            results[hash_type] = time_taken
    
    print("Benchmark Results:")
    for algo, time_taken in results.items():
        print(f"{algo}: {time_taken:.2f} seconds" if time_taken else f"{algo}: Not cracked")

if __name__ == "__main__":
    main()
