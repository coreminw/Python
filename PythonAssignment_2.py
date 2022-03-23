# 가격이 저렴한 쇼핑몰 구하기

aDis = int(input("쇼핑몰 A까지의 거리를 Km단위로 입력하세요: "))
aCost = int(input("쇼핑몰 A의 컴퓨터 가격을 입력하세요: "))
aAll = float(aCost + 2*aDis*(190+1.5*(9160/60)))
print("쇼핑몰 A에서 구입하는 전체 비용은"+str(aAll)+"입니다.")

bDis = int(input("쇼핑몰 B까지의 거리를 Km단위로 입력하세요: "))
bCost = int(input("쇼핑몰 B의 컴퓨터 가격을 입력하세요: "))
bAll = float(bCost + 2*bDis*(190+1.5*(9160/60)))
print("쇼핑몰 A에서 구입하는 전체 비용은"+str(bAll)+"입니다.")

onlineCost = int(input("온라인 컴퓨터 가격을 입력하세요: "))
deliver = int(input("택배 비용을 입력하세요: "))
onAll = float(onlineCost + deliver)
print("쇼핑몰 A에서 구입하는 전체 비용은"+str(onAll)+"입니다.")

if min(aAll, bAll, onAll) == aAll:
    print("A 쇼핑몰에서 구입하는 것이 좋습니다.")
elif min(aAll, bAll, onAll) == bAll:
    print("B 쇼핑몰에서 구입하는 것이 좋습니다.")
else:
    print("온라인에서 구입하는 것이 좋습니다.")



#1km당 1.5분, 1km당 190원이며 1/10 litter