impischdoof = "NMAB OMUICMZB QV LMZ MZLMV ABMPB LQM NWZU ICA TMPU OMJZIVVB PMCBM UCAA LQM OTWKSM EMZLMV NZQAKP OMAMTTMV AMQL HCZ PIVL DWV LMZ ABQZVM PMQAA ZQVVMV UCAA LMZ AKPEMQAA AWTT LIA EMZS LMV UMQABMZ TWJMV LWKP LMZ AMOMV SWUUB DWV WJMV"

def caesar(input):
    frequency = []
    for i in range(26):
        frequency.append(0)
    letters = []
    for i in input.upper():
        if not i == " ":
            letters.append(i)
    for i in letters:
        frequency[ord(i)-65] += 1
    shift = frequency.index(max(frequency)) - 4
    output = ""
    for i in input.upper():
        if i == " " :
            output = output + str(i)
        else:
            shiftedORD = ord(i) - shift
            if shiftedORD < 65:
                shiftedORD = 91 - (65 - shiftedORD)
            elif shiftedORD > 90:
                shiftedORD = 64 + (shiftedORD - 90)
            output = output + str(chr(shiftedORD))
    return output

print(caesar(impischdoof))