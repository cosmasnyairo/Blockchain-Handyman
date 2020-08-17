import hashlib
import json


def hash_string_sha256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    # We hash blocks in our blockchain
    hashable_block = block.__dict__.copy()
    return hash_string_sha256(json.dumps(hashable_block, sort_keys=True).encode())