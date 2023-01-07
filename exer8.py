import re
dna_hair=input()
dna_person=input()
pattern=re.compile('AGCT')
hair_dna_count=len(re.findall(pattern,dna_hair))
person_dna_count=len(re.findall(pattern,dna_person))
if hair_dna_count==person_dna_count:
    print('MATCH')
else:
    print("MISMACTH")