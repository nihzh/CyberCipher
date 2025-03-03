from shiftCipher import *
from affineCipher import *
from vigenereCipher import *
import cryptanalysis as ca


text = """l qhhg d orqjhu whaw ilhog wr whvw wkh fubswdqdobvlv ixqfwlrq ri pb surjudp, lw lv ixoob zulwwhq eb pbvhoi dqg l wklqn lw zloo eh juhdw"""
# print(shiftAnalysis(text))
# print(shiftDec(shiftEnc("byd", 55), 55))



# print(affineEnc("This is my first affine cryptoanalysis text, I think it absolutely will not run properly, but it is a good begin.", 3, 5))
# print(affineDec("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds.", 3, 5))
# print(affineAnalysis("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds."))

# print(affineDec("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH", 3, 5))
# print(affineAnalysis("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"))

# print(vigEnc("i love vigenere and virginia cipher", "abc"))
# print(vigDec("i mqvf xihgnfte bpd wkrhknjc cjrhft", "abc"))
# print(ICCalculate("i mqvf xihgnfte bpd wkrhknjc cjrhft"))

# not success in vig, try upgrade
testtext = "Tiks ju mz hisut bhfjpe dtyqvobpamasju tfzt, J vhjpk jv acuomwtfny xklm pou tuo rrpresny, cwt jv it c gpqd cggjp."
# cuttedStrList = matrixStrCut("".join(filter(str.isalpha, testtext)).lower(), 9)
# cuttedICList = list(map(icCalculate, cuttedStrList))
# avgIC = sum(cuttedICList) / len(cuttedICList)
# print(avgIC)
booktext = """CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW
RVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAK
LXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELX
VRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHR
ZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJT
AMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBI
PEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHP
WQAIIWXNRMGWOIIFKEE"""
# print(sum(v**2 for v in ca.LETTER_PROB.values()))

print(vigAnalysis(booktext))