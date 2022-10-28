from textfrontend.zh_frontend import Frontend

fe = Frontend()
res = fe.get_phonemes('你之前可不是这么说的，一只兔子能做什么，黑兔子呢')
print(res)