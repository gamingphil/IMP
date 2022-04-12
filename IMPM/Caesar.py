input = "NMAB OMUICMZB QV LMZ MZLMV ABMPB LQM NWZU ICA TMPU OMJZIVVB PMCBM UCAA LQM OTWKSM EMZLMV NZQAKP OMAMTTMV AMQL HCZ PIVL DWV LMZ ABQZVM PMQAA ZQVVMV UCAA LMZ AKPEMQAA AWTT LIA EMZS LMV UMQABMZ TWJMV LWKP LMZ AMOMV SWUUB DWV WJMV"



def letterFreq(string):
  # toUpperCase
  lArray = []
  fArray = []
  for i in range(26):  
    fArray.append(0)
  for i in string:
    if not i == " ":
      lArray.append(i)
  for i in lArray:
    fArray[ord(i)-65] = fArray[ord(i)-65] + 1
  return fArray.index(max(fArray))


output = ""
for i in input:
  print("i: "+ i)
  if i == " ":
    output += output + " "
  else:
    output += output + chr(ord(i)+letterFreq(input))
  print("currentOutput: " + output)

print(output)



# print(ord('a'))      