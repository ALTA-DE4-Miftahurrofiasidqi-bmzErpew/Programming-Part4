def ubah_huruf(sentence):
    pattern = ""

    shift = 10
    original_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]
    # print(shifted_alphabet)

    for _, value in enumerate(sentence):
        if value == " ":
            pattern += " "
        else:
            for i, v in enumerate(original_alphabet):
                if v == value:
                    pattern += shifted_alphabet[i]
                    break
    return pattern


# print(
#     ubah_huruf("SEPULSA OKE ALTERRA ACADEMY INDONESIA GOLANG PROGRAMMER")
# )

if __name__ == "__main__":
    print(ubah_huruf("SEPULSA OKE"))  # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY"))  # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA"))  # SXNYXOCSK
    print(ubah_huruf("GOLANG"))  # QYVKXQ
    print(ubah_huruf("PROGRAMMER"))  # ZBYQBKWWOB
    print(ubah_huruf("SEPULSA OKE ALTERRA ACADEMY INDONESIA GOLANG PROGRAMMER"))
