# -*- coding: utf-8 -*-
##拉丁轉寫按dict.py的方式進行，但因不用區分陰陽性字母，故略有不同。

def preprocess_2(word):
    """Prepare a word for function converttomanju."""
    
    ##replace consonants for Chinese loan words with single letter.
    word = word.replace("k'","K")
    word = word.replace("g'","G")
    word = word.replace("h'","H")
    word = word.replace("ts'","T")
    word = word.replace("dz","D")
    word = word.replace("z","Z")
    word = word.replace("sy","S")
    word = word.replace("c'y","C")
    word = word.replace("jy","J")
    word = word.replace("ts","Q")
    
    vowel = ["a", "e", "i", "o", "u", "v"]
    i = 0
    while i < len(word):
        if word[i] == "g": ##case of "ng+consonant" or final "ng".
                if i < len(word) - 1: ##not final "g"
                    if word[i+1] not in vowel and word[i-1] == "n": #letter "g" in "ng+consonant" case
                        word = word[:i-1] + "N" + word[i+1:]
                elif i == len(word) - 1 and word[i-1] == "n": ##final "g", i.e. "ng" at the final part of a word.
                    word = word[:i-1] + "N"
        i += 1
        
    return word
        
def converttomanju(latinword):
    dictmanchuletter = {"a":"ᠠ", "e":"ᡝ", "i":"ᡳ", "o":"ᠣ", "u":"ᡠ", "v":"ᡡ", "n":"ᠨ", "k":"ᡴ", "g":"ᡤ", "h":"ᡥ", "b":"ᠪ", "p":"ᡦ", "s":"ᠰ", "x":"ᡧ", "t":"ᡨ", "d":"ᡩ", "l":"ᠯ", "m":"ᠮ", "c":"ᠴ", "j":"ᠵ", "y":"ᠶ", "K":"ᠺ", "G":"ᡬ", "H":"ᡭ", "r":"ᡵ", "f":"ᡶ", "w":"ᠸ", "T":"ᡮ", "D":"ᡯ", "Z":"ᡰ", "S":"ᠰᡟ", "C":"ᡱ", "J":"ᡷ", "Q":"ᡮᡟ","N":"ᠩ",",":"᠈","<":"︽",".":"᠉",">":"︾","?":"︖","!":"︕",";":"︔",":":"᠄","[":"﹇","]":"﹈","{":"︿","}":"﹀","\\":"᠁","|":"︱","-":" "}
    i = 0
    manjuword = ''
    while i < len(latinword):
        if latinword[i] in dictmanchuletter:
            manjuword = ''.join([manjuword,dictmanchuletter[latinword[i]].decode('utf8')])
        else:
            manjuword = ''.join([manjuword,latinword[i].decode('utf8')])
        i += 1
    return manjuword
    
import csv
import codecs
with open('inputlatin.csv','rb') as input_file:
    record = csv.reader(input_file,delimiter=';')
    for row in record:
        output_row0 = converttomanju(preprocess_2(row[0]))
        output_row2 = converttomanju(preprocess_2(row[2]))
##        print output_row0
##        print row[1].decode('utf8')
        outputrecord = ''
        outputrecord = ''.join([output_row0,";",row[1].decode('utf8'),";",output_row2,";",row[3].decode('utf8'),"\n"])
        with codecs.open('outputmanju.csv','a',encoding="utf-8") as output_file:
            output_file.write(outputrecord)

