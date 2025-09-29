import random
import string

def generate_id(prefix):
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}-{suffix}"