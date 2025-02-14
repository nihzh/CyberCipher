from shiftCipher import *
from affineCipher import *


text = """l qhhg d orqjhu whaw ilhog wr whvw wkh fubswdqdobvlv ixqfwlrq ri pb surjudp, lw lv ixoob zulwwhq eb pbvhoi dqg l wklqn lw zloo eh juhdw"""
print(shiftAnalysis(text))
# print(shiftDec(shiftEnc("byd", 55), 55))



# print(affineEnc("This is my first affine cryptoanalysis text, I think it absolutely will not run properly, but it is a good begin.", 3, 5))
# print(affineDec("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds.", 3, 5))
# print(affineAnalysis("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds."))

print(affineDec("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH", 3, 5))
print(affineAnalysis("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"))