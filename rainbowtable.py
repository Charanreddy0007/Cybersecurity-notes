import hashlib
import random

# =========================
# Configuration
# =========================
PASSWORD_SPACE = 10000      # 0000 - 9999
CHAIN_LENGTH = 100
NUM_CHAINS = 200
TABLE_FILE = "rainbow_table.txt"

# =========================
# Hash Function (MD5)
# =========================
def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# =========================
# Reduction Function
# =========================
def reduction_function(hash_value, step):
    # Convert hash to integer
    num = int(hash_value, 16)
    
    # Mix step into reduction ("rainbow" effect)
    reduced = (num + step) % PASSWORD_SPACE
    
    return f"{reduced:04d}"

# =========================
# Generate Single Chain
# =========================
def generate_chain(start_password):
    password = start_password
    
    for step in range(CHAIN_LENGTH):
        hash_val = md5_hash(password)
        password = reduction_function(hash_val, step)
    
    return start_password, password

# =========================
# Generate Rainbow Table
# =========================
def generate_rainbow_table():
    table = {}

    for _ in range(NUM_CHAINS):
        start = f"{random.randint(0, PASSWORD_SPACE-1):04d}"
        chain_start, chain_end = generate_chain(start)
        table[chain_start] = chain_end

    # Save table to file
    with open(TABLE_FILE, "w") as f:
        for start, end in table.items():
            f.write(f"{start}:{end}\n")

    print(f"Rainbow table saved to {TABLE_FILE}")
    return table

# =========================
# Load Rainbow Table
# =========================
def load_rainbow_table():
    table = {}
    with open(TABLE_FILE, "r") as f:
        for line in f:
            start, end = line.strip().split(":")
            table[start] = end
    return table

# =========================
# Crack Hash
# =========================
def crack_hash(target_hash, table):
    for position in reversed(range(CHAIN_LENGTH)):
        temp_hash = target_hash
        
        # Simulate chain from different positions
        for step in range(position, CHAIN_LENGTH):
            password_candidate = reduction_function(temp_hash, step)
            temp_hash = md5_hash(password_candidate)
        
        # Check if matches chain end
        for start, end in table.items():
            if end == password_candidate:
                # Regenerate full chain from start
                pwd = start
                for step in range(CHAIN_LENGTH):
                    h = md5_hash(pwd)
                    if h == target_hash:
                        return pwd
                    pwd = reduction_function(h, step)
    
    return None

# =========================
# Run Demo
# =========================
if __name__ == "__main__":
    print("Generating rainbow table...")
    table = generate_rainbow_table()

    test_password = "1234"
    test_hash = md5_hash(test_password)
    print(f"\nTarget hash: {test_hash}")

    loaded_table = load_rainbow_table()
    cracked = crack_hash(test_hash, loaded_table)

    if cracked:
        print(f"Password cracked: {cracked}")
    else:
        print("Password not found in table.")