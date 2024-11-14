flag = "d1a7b589fe2349f9c8b41a6e7f3d9c5bb2a4f1c1f8e0234da3b49e8c5d7b6c9f"
guess = input('Enter Flag:\n')
if guess == flag:
    print('Congratulations, you found the Flag!')
elif guess == 'Hint1':
    print('After reviewing the passwords and codenames, you noticed that they appear to be encrypted by the same mechanism.')
elif guess == 'Hint2':
    print('You reach out to a coworker who previously worked on a case involving PANTHEON. He told you that they like to use keyed Caesar Ciphers for encryption. Review the case for possible keywords.')
else:
    print('Sorry, that is incorrect. Please try again.')