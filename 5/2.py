from common import find_hash

password = list(8 * '_')
hasher = find_hash()
while '_' in password:
    hashed = next(hasher)
    try:
        index = int(hashed[5])
        if password[index] == '_':
            password[index] = hashed[6]
    except (ValueError, IndexError):
        pass

print(''.join(password))
