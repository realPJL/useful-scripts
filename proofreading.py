#pip install lmproof
import lmproof

def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))

input = input("Enter text here: ")

proofread(input)

# TODO fix error
# E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory.