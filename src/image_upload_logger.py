def log(username, filename, link):
    with open("userlist.csv", "a+") as f:
        f.write('\n')
        f.write(f'{username},{filename},{link}')