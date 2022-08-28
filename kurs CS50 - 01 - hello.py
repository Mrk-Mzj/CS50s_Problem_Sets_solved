
# ask user for a name
username = input("What's your name? ")

# clean white spaces and capitalize the first letter of every word
username = username.strip().title()

# write user name
print(f'Hello {username}!')             # f na początku wskazuje na użycie formatowanego stringa
print('Hello ' + username + '!')        # ta wersja przekazuje jeden długi argument (+)
print('Hello ', username, '!', sep='')  # ta kilka argumentów (,) a sep usuwa spacje domyślnie dodawane między argumentami

