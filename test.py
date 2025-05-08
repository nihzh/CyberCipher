from algorithms import affineCipher
from algorithms import shiftCipher
from algorithms import vigenereCipher
from algorithms import cryptanalysis


# text = """l qhhg d orqjhu whaw ilhog wr whvw wkh fubswdqdobvlv ixqfwlrq ri pb surjudp, lw lv ixoob zulwwhq eb pbvhoi dqg l wklqn lw zloo eh juhdw"""
# # print(shiftAnalysis(text))
# # print(shiftDec(shiftEnc("byd", 55), 55))

print(vigenereCipher.vigAnalysis("a"))

# # print(affineEnc("This is my first affine cryptoanalysis text, I think it absolutely will not run properly, but it is a good begin.", 3, 5))
# # print(affineCipher.affineDec("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds.", 3, 5))
# # print(affineCipher.affineAnalysis("Kadh dh pz udehk fuudsr lezykvfsfmzhdh krwk, D kadsj dk fihvmnkrmz tdmm svk ens yevyremz, ink dk dh f xvvo irxds."))

# # print(affineDec("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH", 3, 5))
# # print(affineCipher.affineAnalysis("FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"))

# # print(vigEnc("i love vigenere and virginia cipher", "abc"))
# # print(vigDec("i mqvf xihgnfte bpd wkrhknjc cjrhft", "abc"))
# # print(ICCalculate("i mqvf xihgnfte bpd wkrhknjc cjrhft"))

# # not success in vig, try upgrade
# testtext = "Tiks ju mz hisut bhfjpe dtyqvobpamasju tfzt, J vhjpk jv acuomwtfny xklm pou tuo rrpresny, cwt jv it c gpqd cggjp."
# # cuttedStrList = matrixStrCut("".join(filter(str.isalpha, testtext)).lower(), 9)
# # cuttedICList = list(map(icCalculate, cuttedStrList))
# # avgIC = sum(cuttedICList) / len(cuttedICList)
# # print(avgIC)
# booktext = """CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW
# RVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAK
# LXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELX
# VRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHR
# ZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJT
# AMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBI
# PEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHP
# WQAIIWXNRMGWOIIFKEE"""
# test2 = "Xju mys fphtgt viqqd llg xivnbvf, tcyhxnpn llg iec np omiu ez swcuyi cdx tnpr. S kgdnpj dywibu lyxvswh vxy pjccww, eqlvdkuy xju mgjpa gj dbisrkuy jneqiwu. Iavfi wlntwwh vxymw gcwrkda wtpnk, ajyfi yjl vmujury jbe sh jbi hkaq jctyh npag xju vehmnjswdx. Xmg dgvnt mijolv xq fuyxg, leftqwmsi azi vhurvwpdmvo ij yjl esouhx. Fu zleti vilcu ls vmcrpnl sfqly, e xguki qv jifel kivjfii qcwv vxy pfpkkgcfy. My yhk e ruljjea wzgdcrl, c ywqkdxiw qm fevkli'x dlsyvo uri vow wkcjpj lvqw kj vvnpnk. Mp jbey uljipu miyvpfk, vygi kgsl mpvcrnvl, srf mivwklk qgbnii cdsc"
# # print(sum(v**2 for v in ca.LETTER_PROB.values()))

# # print(vigenereCipher.vigAnalysis(test2))

# # print(cryptanalysis.getLetterEqus([19]))
# # print(52 % 26)
# # print('a'.toLowerCase().charCodeAt(0))




# # from collections import defaultdict
# # from math import gcd
# # from functools import reduce

# # def find_repeated_sequences(ciphertext, length=3):
# #     """
# #     查找密文中所有重复的子串及其起始索引
# #     """
# #     sequences = defaultdict(list)
    
# #     for i in range(len(ciphertext) - length + 1):
# #         substring = ciphertext[i:i + length]
# #         sequences[substring].append(i)

# #     # 只保留出现多次的子串
# #     return {key: value for key, value in sequences.items() if len(value) > 1}

# # def calculate_distances(repeated_sequences):
# #     """
# #     计算相同子串在密文中出现的间隔（即索引之间的距离）
# #     """
# #     distances = []
    
# #     for indexes in repeated_sequences.values():
# #         for i in range(len(indexes) - 1):
# #             distances.append(indexes[i + 1] - indexes[i])
    
# #     return distances

# # def find_key_length(ciphertext, min_seq_len=3):
# #     """
# #     执行 Kasiski 检测法来估计可能的密钥长度
# #     """
# #     # 1. 找到重复的子串
# #     repeated_sequences = find_repeated_sequences(ciphertext, min_seq_len)
    
# #     if not repeated_sequences:
# #         print("未找到足够的重复子串，请尝试更短的序列长度。")
# #         return None

# #     # 2. 计算重复子串间的距离
# #     distances = calculate_distances(repeated_sequences)

# #     if not distances:
# #         print("未找到足够的距离数据，可能密钥较长或密文较短。")
# #         return None

# #     # 3. 计算所有距离的最大公约数（GCD）
# #     possible_key_length = reduce(gcd, distances)
    
# #     return possible_key_length if possible_key_length > 1 else None

# # # 示例密文（伪造的弗吉尼亚加密密文）
# # ciphertext = "Poakhllk wojnyx cy ut ytwxsvnoit gknnij vgmkx uh zbk Wgyyux wojnyx, ut ytwxsvnoit uraulonng zbgn amkm g mkloyy il Wgyyux wojnyxm zi lixg g wojnyx urjnuhyz, utx hyritay nu u ycsjry lixg uz sorno-ngvry icvbkly."

# # # 运行 Kasiski 分析
# # key_length = find_key_length(ciphertext)

# # if key_length:
# #     print(f"prob: {key_length}")
# # else:
# #     print("cannot sure")

# plainText = ["asdfasdfasdf", "qwerqwerqwer"]
# if len(plainText) > 1:
#         outputText = ""
#         for text, index in enumerate(plainText):
#             outputText += f'Result {text}: {{"{index}"}}\n'
#         plainText = outputText
# print(plainText)