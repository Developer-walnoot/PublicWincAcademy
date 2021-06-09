# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
mainLangSZ = "German"
mainLangSP = "Spanish"
capitalLenSZ = 4
capitalLenSP = 6
gdpSZ = 580000000000
gdpSP = 1778000000000
popGrowthSP = .67
popGrowthSZ = .66

popGrowthMin = 1.0

popcountSP = 50000000
popcountSZ = 8400000
popcount10mil = 1000000
#

prevalentReligionSZ = "Roman_catholic"
prevalentReligionSP = "Roman_catholic"

print(mainLangSZ == mainLangSP)
print(prevalentReligionSZ == prevalentReligionSP)
print(capitalLenSZ != capitalLenSP)
print(gdpSZ == gdpSP)
print(popGrowthMin > popGrowthSP and popGrowthMin > popGrowthSZ )
print(popcount10mil < popcountSP or popcount10mil < popcountSZ)
print(popcount10mil < popcountSP and popcount10mil < popcountSZ)


