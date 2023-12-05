from tal import talents

skill_set=input("Choose a kit: ").lower

if skill_set=="kit one":
    skill_set.gain("Health increase by 130% of base, attack decrease 20%")
elif skill_set=="kit two":
    skill_set.gain("Heath decreased by 30% of base, attack increase by 50%")
elif skill_set=="kit three":
    skill_set.gain("Health increase by 200% of base, cannot attack next 3 turns")
else:
    skill_set.gain("Health decrease by 50%, attack increase by 130%")