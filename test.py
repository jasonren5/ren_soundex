import ren_soundex as soundex
import testclass
s = soundex.soundexer()
print(s.soundex("jjjjj"))
print(s.soundex(""))
print(s.soundex("125125"))
print(s.soundex("-1125"))
print(s.soundex("asfasfasfasf"))
print(s.soundex("ashcraftbbbbb"))
print(s.soundex("ashcroftbbbbb"))
print(s.soundex("bbbbbbbbbb"))
print(s.soundex("Honeyman"))
