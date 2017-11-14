braille = ([
    [1, 0, 0, 0, 0, 0], # 00: a
    [1, 0, 1, 0, 0, 0], # 01: b
    [1, 1, 0, 0, 0, 0], # 02: c
    [1, 1, 0, 1, 0, 0], # 03: d
    [1, 0, 0, 1, 0, 0], # 04: e
    [1, 1, 0, 1, 0, 0], # 05: f
    [1, 1, 1, 1, 0, 0], # 06: g
    [1, 0, 1, 1, 0, 0], # 07: h
    [0, 1, 1, 0, 0, 0], # 08: i
    [0, 1, 1, 1, 0, 0], # 09: j
    [1, 0, 0, 0, 1, 0], # 10: k
    [1, 0, 1, 0, 1, 0], # 11: l
    [1, 1, 0, 0, 1, 0], # 12: m
    [1, 1, 0, 1, 1, 0], # 13: n
    [1, 0, 0, 1, 1, 0], # 14: o
    [1, 1, 1, 0, 1, 0], # 15: p
    [1, 1, 1, 1, 1, 0], # 16: q
    [1, 0, 1, 1, 1, 0], # 17: r
    [0, 1, 1, 0, 1, 0], # 18: s
    [0, 1, 1, 1, 1, 0], # 19: t
    [1, 0, 0, 0, 1, 1], # 20: u
    [1, 0, 1, 0, 1, 1], # 21: v
    [0, 1, 1, 1, 1, 1], # 22: w
    [1, 1, 0, 0, 1, 1], # 23: x
    [1, 1, 0, 1, 1, 1], # 24: y
    [1, 0, 0, 1, 1, 1], # 25: z
    [0, 0, 1, 0, 0, 0], # 26: ,
    [0, 0, 1, 1, 0, 1], # 27: .
    [0, 0, 1, 1, 0, 0], # 28: -
    [0, 0, 1, 0, 1, 1], # 29: ?
    [0, 0, 0, 0, 1, 1], # 30: _
    [0, 0, 1, 1, 1, 0], # 31: !
    [0, 0, 0, 0, 1, 0]  # 32: "
])

english = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r' , 's', 't',
           'u' , 'v', 'w', 'x', 'y', 'z', ',', '-', '?', '_',
           '!', '"')

def isCapital ( char ):
    capitals = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z')

    for c in capitals:
        if c == char:
            return True

    return False


def engToBraille ( string ):
    # List which will contain braille in form of lists
    sentence = []

    for char in string:
        if isCapital(char): # capital prefix
            sentence.append([0,0,0,0,0,1])
        elif char.isnumeric(): # number prefix
            sentence.append([0,1,0,1,1,1])

        count = 0
        for c in english:
            if c == char.lower():
                sentence.append(braille[count])
                break
            count = count + 1

    # trim white space from end

    return sentence



def main():
    test = engToBraille("Hello")
    for t in test:
        print(t)

main()
