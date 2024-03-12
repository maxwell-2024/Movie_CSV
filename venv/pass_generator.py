import random
import string


def pw_gen(*, pass_length=8, letters=True, symbols=True, numbers=True, duplicates=False):
    if pass_length < 8:
        print('PW length should be at least 8 symbols')
        return
    groups = ['let', symbols, numbers]  # To create number of
    groups_num = 0
    for g in groups:
        if g:
            groups_num += 1
    amount = pass_length // groups_num
    after = pass_length - amount * groups_num
    pw = ''

    if letters:
        pw += ''.join(random.choice(string.ascii_letters) for i in range(amount))
    else:
        pw += ''.join(random.choice(string.ascii_lowercase) for i in range(amount))
    if numbers:
        pw += ''.join(random.choice(string.digits) for i in range(amount))
    if symbols:
        pw += ''.join(random.choice("!@#$%^&*()+") for i in range(amount))
    if pass_length - after != 0:
        pw += ''.join(random.choice(string.ascii_lowercase) for i in range(after))
    final_password = ''.join(random.choice(pw) for i in range(len(pw)))
    if not duplicates:
        while True:
            unique = ''.join(set(final_password))
            if len(unique) != pass_length:
              final_password = unique + random.choice(string.ascii_lowercase)
              continue
            break
    return final_password

password = pw_gen(pass_length=40, letters=True, symbols=True, numbers=True, duplicates=False)

print(f"Password: {password}\nPassword length: {len(password)}")



