from percentage_calculation import Percentage
from deciphering import Decoder
from identifying_matches import MatchCount
from level_attach import AttachLevel
# text-classification/src/words_lists.txt

# class ClassifierManager:
#     def __init__(self):
text = "did you see the footage yesterday entire family is forced out again displacement never really ended since the nachba right the occupation keeps producing refugees and unrwa is barely able to keep up schools clinics everything is under strain and while leaders debate ceasefire terms kids in Gaza live under constant fear it's more than politics its survival that's why resistance especially non-violent resistance Matters from protests to Freedom flotilla missions people are reminding the world that Palestinians aren't invisible and when people join boycotts or call out a part-time it shifts The Narrative every action counts we just need to keep reminding people this is a humanitarian struggle not some abstract conflict"
Hostile_list = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
Non_hostile_list = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='

p = Percentage
d = Decoder
m =MatchCount
l = AttachLevel

l1 = d(Hostile_list).decoding_code()
l2 = d(Non_hostile_list).decoding_code()
mch = m(text,l1,l2).match_count()
pr = p(mch[0],mch[1],len(text)).percentage_calculator()

f = l(pr).attach_by_percent()

print(f)

