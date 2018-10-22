import Ren_Soundex as soundex
import testclass
s = soundex.soundexer()
print(s.soundex("jjjjj"))
print(s.soundex(""))
print(s.soundex("125125"))
print(s.soundex("-1125"))
print(s.soundex("asfasfasfasf"))
print(s.soundex("ashcraft"))
print(s.soundex("ashcroft"))
