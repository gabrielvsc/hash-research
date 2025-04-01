import time
import hashlib
from tqdm import tqdm

def brute_force_attack(target_hash, hash_function, wordlist):
    """Attempts to break a hash using brute force with a wordlist."""
    start_time = time.time()
    
    for word in tqdm(wordlist, desc=f"Cracking {hash_function}"):
        word = word.strip()
        
        try:
            if hash_function == "MD5" and hashlib.md5(word.encode()).hexdigest() == target_hash:
                return time.time() - start_time
            if hash_function == "SHA-1" and hashlib.sha1(word.encode()).hexdigest() == target_hash:
                return time.time() - start_time
            if hash_function == "SHA-256" and hashlib.sha256(word.encode()).hexdigest() == target_hash:
                return time.time() - start_time
        except Exception as e:
            print(f"Error during brute force attack: {e}")
            return None
    
    return None
