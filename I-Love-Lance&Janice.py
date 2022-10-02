def solution(x):
    # Iterate over string to append characters
    l = len(x)
    for character in x:
        y = decrypt(character)
        x += y
    # cut the previous
    return x[l:]


def decrypt(character):
    # return the decrypt character
    if 'a' <= character <= 'z':
        # equation: ord(char)+ord(shouldBe) = ord(a)+ ord(z)
        return chr(ord('a') + ord('z') - ord(character))
    else:
        return character

testString = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
testCase = solution(testString)
print(testCase)
