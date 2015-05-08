#this is to make sure colors match 

import random
import numpy as np

#this function was created mainly because we already assigned colors to one of our graphs and it we need to preserve color scheme
def initializeAlreadyColoredSizes():
	#this usz was created from nodes 5 density .25 umax 10 stackedBar_by_u
	usz = set([1, 2, 3, 4, 5, 6, 7, 9, 12, 14, 16, 913, 146, 131, 21, 132, 29, 33, 34, 933, 38, 48, 52, 64, 961, 322, 584, 140, 79, 84, 85, 986, 91, 992, 993, 994, 995, 996, 997, 998, 999, 232, 1001, 18, 1000, 19, 632])
	sortusz = sorted(usz)
	predetermined_color_list = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), (0.904005064928743, 0.3038725882767085, 0.9399279068775889), (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), (0.5934259725250017, 0.6259544064286037, 0.8943937276483482), (0.1834548561930609, 0.8625908063396674, 0.2808367027257399), (0.9522043509564118, 0.8383482335114356, 0.04624824811210648), (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), (0.4681299494331541, 0.7560613323413682, 0.10402356714939609), (0.9439367271803931, 0.9189366721892608, 0.7886855210193017), (0.6980608691309792, 0.6296583577840691, 0.10122715703511265), (0.7530798564980008, 0.14571022694658842, 0.1558625362484024), (0.2646659319053375, 0.5140308942688593, 0.6505540444073039), (0.32532392896062434, 0.6771986595824758, 0.6804464385760941), (0.561698593156714, 0.8903102946046827, 0.5464538203577384), (0.06195801226204156, 0.4085195670330185, 0.16777660887869106), (0.4862983226162474, 0.9266576030195525, 0.5200207123141651), (0.8823494781169269, 0.8602854575796756, 0.46655973657031047), (0.060221542213292456, 0.01914731167580286, 0.3055281480683151), (0.766342531208258, 0.9245825374766737, 0.37031711910405163), (0.8918452889529781, 0.3489446890522606, 0.5363393265500108), (0.39140968224876604, 0.20490073625104321, 0.49724364222766826), (0.15440849286794844, 0.5109256317494821, 0.918663018768346), (0.46426804376009356, 0.5040025154668996, 0.18863898344256602), (0.6418660472107188, 0.19387172503903427, 0.08253445229983347), (0.31722667708720487, 0.441657298575016, 0.7178566635952561), (0.606928934759279, 0.18954053420608696, 0.3971704554820378), (0.4417364105098468, 0.4369407216947674, 0.16241194628082245), (0.8107807623400896, 0.3099877573648637, 0.435731436486533), (0.2329089726116761, 0.10130531525410325, 0.5097643277292452), (0.5665782970092119, 0.22826862385734814, 0.38958016270033535), (0.48137410722891594, 0.09467528600649266, 0.5375593747271779), (0.09726368948435926, 0.8369969882905206, 0.07986516857033343), (0.2694751359724161, 0.45498770799919086, 0.6448059472136883), (0.38997444066817866, 0.9781779063852679, 0.874217562859495), (0.7051477513703358, 0.5702924839652445, 0.24312377606293833), (0.5709641799914025, 0.743539099020067, 0.8261827299024898), (0.8178345478004484, 0.981435239104708, 0.6544046775407857), (0.4320231702054077, 0.07210261858206857, 0.07920415400870395), (0.5627424217341767, 0.1968727734442548, 0.3595950676513303), (0.20981445390600095, 0.30693865142032595, 0.48997043645185046), (0.9241714458529445, 0.8143896488420276, 0.7663922292951993), (0.1885301360711723, 0.8389391807577213, 0.0755369071561598)]
	already_colored_sizes = {}
	for i in range(len(usz)):
		already_colored_sizes[sortusz[i]]= predetermined_color_list[i]
	print already_colored_sizes
	return already_colored_sizes


#this function is for adding new sizes and colors to already_colored_sizes
def addSizeColor(newusz,already_colored_sizes):
	for size in newusz:
		if size not in already_colored_sizes:
			already_colored_sizes[size]=((random.random(),random.random(),random.random()))
	print already_colored_sizes
	return already_colored_sizes

#this function is for outputing a color list for the size set I am interested in
def outputcolorlist(usz,already_colored_sizes):
	tempdict = {}
	for size in usz:
		tempdict[size] = already_colored_sizes[size]
	colorlist = []
	for x in np.sort(tempdict.keys()):
		colorlist.append(tempdict[x])
	print colorlist
	return colorlist

#after adding
#stackedBar_by_u
#stackedBar_by_density: 
#	5 nodes
#		u = 2
#		u = 3

usz3 = set([128, 1, 2, 3, 4, 5, 902, 7, 11, 12, 14, 16, 918, 24, 921, 154, 31, 34, 292, 38, 951, 132, 64, 961, 707, 68, 583, 55, 76, 975, 56, 331, 860, 990, 992, 272, 996, 102, 358, 999, 1000, 1001, 631, 249, 123, 998])
#already_colored_sizes = {1: (0.9769448735268946, 0.6468696110452877, 0.2151452804329661), 2: (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), 3: (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), 4: (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), 5: (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), 6: (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), 7: (0.904005064928743, 0.3038725882767085, 0.9399279068775889), 8: (0.39140782566655674, 0.7613012099948101, 0.7475874114794775), 9: (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), 10: (0.8599446540919113, 0.2080708213188862, 0.8893517695418856), 11: (0.022700048163251885, 0.658455757390323, 0.45194508876647577), 12: (0.5934259725250017, 0.6259544064286037, 0.8943937276483482), 13: (0.12487596822954139, 0.1286185769691658, 0.6973677590395778), 14: (0.1834548561930609, 0.8625908063396674, 0.2808367027257399), 15: (0.7072265637451247, 0.795648339142106, 0.4662593453344923), 16: (0.9522043509564118, 0.8383482335114356, 0.04624824811210648), 18: (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), 19: (0.4681299494331541, 0.7560613323413682, 0.10402356714939609), 20: (0.255653326552158, 0.5961600354559602, 0.1137780460753558), 21: (0.9439367271803931, 0.9189366721892608, 0.7886855210193017), 24: (0.8995777049552036, 0.8978927956586498, 0.7239642220024304), 25: (0.40222983289275105, 0.9345684739537153, 0.566491195073673), 26: (0.05133937324768556, 0.7727016141102293, 0.599682730400552), 27: (0.6713347042221948, 0.44827277249822983, 0.5758028025623169), 28: (0.2536385202352366, 0.6050891521826539, 0.20807572283377163), 29: (0.6980608691309792, 0.6296583577840691, 0.10122715703511265), 33: (0.7530798564980008, 0.14571022694658842, 0.1558625362484024), 34: (0.2646659319053375, 0.5140308942688593, 0.6505540444073039), 35: (0.1646147271511358, 0.5684305293900335, 0.4909183445246943), 37: (0.41106101124915306, 0.6905698281245495, 0.6635168303852723), 38: (0.32532392896062434, 0.6771986595824758, 0.6804464385760941), 39: (0.9525519916784567, 0.7511035215433497, 0.8304180841797634), 41: (0.21112416388960142, 0.7892901500348418, 0.5183165258146284), 46: (0.2687445198466347, 0.47096330276612686, 0.7802761303443152), 47: (0.35582076909521787, 0.8745064854695166, 0.3545516591571266), 48: (0.561698593156714, 0.8903102946046827, 0.5464538203577384), 50: (0.5444611719681884, 0.7322772657961953, 0.17556307524789427), 51: (0.8975192077387196, 0.4256266095653507, 0.9580605810028985), 52: (0.06195801226204156, 0.4085195670330185, 0.16777660887869106), 53: (0.9061819404330758, 0.4819595022335398, 0.7355265783007073), 54: (0.26867538636637267, 0.517149856740674, 0.6730945199483196), 56: (0.1969119108920101, 0.7691832236626523, 0.8581500511883019), 58: (0.24317906305210757, 0.07199642368662595, 0.5671977646914638), 59: (0.9764918101388413, 0.3806367183382917, 0.5203279005692817), 60: (0.044363631256075564, 0.9991717511296541, 0.22719110673281473), 575: (0.8652356351587394, 0.853185868084153, 0.32231981978946056), 64: (0.4862983226162474, 0.9266576030195525, 0.5200207123141651), 65: (0.5526489158835673, 0.9263316945221866, 0.7708982914425199), 68: (0.21853742909113694, 0.6863672034685054, 0.28906788161042285), 583: (0.33249893828748023, 0.5574402721532626, 0.048355320787969336), 584: (0.4417364105098468, 0.4369407216947674, 0.16241194628082245), 79: (0.8823494781169269, 0.8602854575796756, 0.46655973657031047), 84: (0.060221542213292456, 0.01914731167580286, 0.3055281480683151), 85: (0.766342531208258, 0.9245825374766737, 0.37031711910405163), 87: (0.13948591895527063, 0.8844404174150958, 0.20739570597562296), 91: (0.8918452889529781, 0.3489446890522606, 0.5363393265500108), 119: (0.8606249030204752, 0.006002024038369358, 0.8926479044904958), 632: (0.8107807623400896, 0.3099877573648637, 0.435731436486533), 126: (0.5169187761292617, 0.05239930912138857, 0.13220206501097675), 131: (0.39140968224876604, 0.20490073625104321, 0.49724364222766826), 132: (0.15440849286794844, 0.5109256317494821, 0.918663018768346), 134: (0.6802337626345111, 0.3952319177096246, 0.9577912878133846), 136: (0.5429750037107149, 0.2516054077133302, 0.6383395346264112), 140: (0.46426804376009356, 0.5040025154668996, 0.18863898344256602), 144: (0.669049415010293, 0.6601594798409904, 0.3690336138842457), 146: (0.6418660472107188, 0.19387172503903427, 0.08253445229983347), 147: (0.9171177970189475, 0.7570401635513673, 0.41473173765212656), 150: (0.8514416943359722, 0.26776326080817003, 0.42656484426039165), 153: (0.563959718408767, 0.16805776410240414, 0.2368635130939043), 154: (0.6077128018278273, 0.7114298585206303, 0.011655130253268031), 194: (0.9457583531121714, 0.41934982666062404, 0.3692802897910529), 725: (0.006325524188502296, 0.18950234542615196, 0.23926750268622843), 732: (0.5527651291905299, 0.5746966496279889, 0.43171636233396815), 736: (0.5344327591142222, 0.5257392860926776, 0.5651227710291419), 737: (0.7028212878281531, 0.9371346737132197, 0.15804097206531542), 232: (0.31722667708720487, 0.441657298575016, 0.7178566635952561), 240: (0.41580848148241223, 0.04618512467563829, 0.5158900558093626), 298: (0.5344828886572797, 0.6263131982198099, 0.8734018104264674), 307: (0.7919826102084409, 0.5608948323741435, 0.8863426580950163), 308: (0.4715901668807123, 0.22691497224040869, 0.8324257857284412), 322: (0.606928934759279, 0.18954053420608696, 0.3971704554820378), 331: (0.43828274661059363, 0.6307222593349302, 0.2340955475172376), 335: (0.3875743287260326, 0.4336592646622611, 0.18786909694048148), 857: (0.6780319762513275, 0.7704555463533739, 0.28812460936085504), 357: (0.4911512658500157, 0.36885328979544607, 0.16493510014450008), 902: (0.26236788359719754, 0.17529748970429215, 0.6484863208369795), 394: (0.02984494188497888, 0.8162917062597478, 0.11484767161474563), 395: (0.06373733176053709, 0.05828579994431693, 0.5276576646723787), 913: (0.2329089726116761, 0.10130531525410325, 0.5097643277292452), 409: (0.7846373211228662, 0.7094511532689909, 0.20386715797977129), 925: (0.115824596742378, 0.34992381657932414, 0.6153763241914337), 932: (0.6128682578052749, 0.25593752365317624, 0.4275747216942438), 933: (0.5665782970092119, 0.22826862385734814, 0.38958016270033535), 936: (0.3984406181611808, 0.06088973642585682, 0.8766893533007929), 942: (0.23548730894370484, 0.5851340605722368, 0.945897539314606), 943: (0.1818978404565259, 0.04768290319210333, 0.892897952279543), 72: (0.7185498068459529, 0.42178934105231114, 0.7170822708612701), 954: (0.24297204338780298, 0.652460465843344, 0.4921529562664547), 957: (0.44375448350658886, 0.9279067963165427, 0.6842608816352503), 961: (0.48137410722891594, 0.09467528600649266, 0.5375593747271779), 963: (0.7023622379209911, 0.17828223889557793, 0.10718503235353127), 966: (0.8259245621037714, 0.42802889162999047, 0.38258746898149265), 970: (0.4945168465360159, 0.40294280549563233, 0.374481199283637), 974: (0.08719382781846197, 0.7675988748519565, 0.8076046247368227), 976: (0.74224238574635, 0.23427758549595035, 0.7699090417859882), 986: (0.09726368948435926, 0.8369969882905206, 0.07986516857033343), 991: (0.9289417957628747, 0.21033188329558805, 0.44865447618425736), 992: (0.2694751359724161, 0.45498770799919086, 0.6448059472136883), 993: (0.38997444066817866, 0.9781779063852679, 0.874217562859495), 994: (0.7051477513703358, 0.5702924839652445, 0.24312377606293833), 995: (0.5709641799914025, 0.743539099020067, 0.8261827299024898), 996: (0.8178345478004484, 0.981435239104708, 0.6544046775407857), 997: (0.4320231702054077, 0.07210261858206857, 0.07920415400870395), 998: (0.5627424217341767, 0.1968727734442548, 0.3595950676513303), 999: (0.20981445390600095, 0.30693865142032595, 0.48997043645185046), 1000: (0.9241714458529445, 0.8143896488420276, 0.7663922292951993), 1001: (0.1885301360711723, 0.8389391807577213, 0.0755369071561598), 490: (0.42060664576563456, 0.8132783716104773, 0.07824296338425984)}

#addSizeColor(usz3,already_colored_sizes)
already_colored_sizes = {1: (0.9769448735268946, 0.6468696110452877, 0.2151452804329661), 2: (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), 3: (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), 4: (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), 5: (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), 6: (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), 7: (0.904005064928743, 0.3038725882767085, 0.9399279068775889), 8: (0.39140782566655674, 0.7613012099948101, 0.7475874114794775), 9: (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), 10: (0.8599446540919113, 0.2080708213188862, 0.8893517695418856), 11: (0.022700048163251885, 0.658455757390323, 0.45194508876647577), 12: (0.5934259725250017, 0.6259544064286037, 0.8943937276483482), 13: (0.12487596822954139, 0.1286185769691658, 0.6973677590395778), 14: (0.1834548561930609, 0.8625908063396674, 0.2808367027257399), 15: (0.7072265637451247, 0.795648339142106, 0.4662593453344923), 16: (0.9522043509564118, 0.8383482335114356, 0.04624824811210648), 18: (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), 19: (0.4681299494331541, 0.7560613323413682, 0.10402356714939609), 20: (0.255653326552158, 0.5961600354559602, 0.1137780460753558), 21: (0.9439367271803931, 0.9189366721892608, 0.7886855210193017), 24: (0.8995777049552036, 0.8978927956586498, 0.7239642220024304), 25: (0.40222983289275105, 0.9345684739537153, 0.566491195073673), 26: (0.05133937324768556, 0.7727016141102293, 0.599682730400552), 27: (0.6713347042221948, 0.44827277249822983, 0.5758028025623169), 28: (0.2536385202352366, 0.6050891521826539, 0.20807572283377163), 29: (0.6980608691309792, 0.6296583577840691, 0.10122715703511265), 31: (0.2556726736236199, 0.2104548430331603, 0.8512080303034044), 33: (0.7530798564980008, 0.14571022694658842, 0.1558625362484024), 34: (0.2646659319053375, 0.5140308942688593, 0.6505540444073039), 35: (0.1646147271511358, 0.5684305293900335, 0.4909183445246943), 37: (0.41106101124915306, 0.6905698281245495, 0.6635168303852723), 38: (0.32532392896062434, 0.6771986595824758, 0.6804464385760941), 39: (0.9525519916784567, 0.7511035215433497, 0.8304180841797634), 41: (0.21112416388960142, 0.7892901500348418, 0.5183165258146284), 46: (0.2687445198466347, 0.47096330276612686, 0.7802761303443152), 47: (0.35582076909521787, 0.8745064854695166, 0.3545516591571266), 48: (0.561698593156714, 0.8903102946046827, 0.5464538203577384), 50: (0.5444611719681884, 0.7322772657961953, 0.17556307524789427), 51: (0.8975192077387196, 0.4256266095653507, 0.9580605810028985), 52: (0.06195801226204156, 0.4085195670330185, 0.16777660887869106), 53: (0.9061819404330758, 0.4819595022335398, 0.7355265783007073), 54: (0.26867538636637267, 0.517149856740674, 0.6730945199483196), 55: (0.5151791425316585, 0.8441590818250184, 0.22176363661186171), 56: (0.1969119108920101, 0.7691832236626523, 0.8581500511883019), 58: (0.24317906305210757, 0.07199642368662595, 0.5671977646914638), 59: (0.9764918101388413, 0.3806367183382917, 0.5203279005692817), 60: (0.044363631256075564, 0.9991717511296541, 0.22719110673281473), 575: (0.8652356351587394, 0.853185868084153, 0.32231981978946056), 64: (0.4862983226162474, 0.9266576030195525, 0.5200207123141651), 65: (0.5526489158835673, 0.9263316945221866, 0.7708982914425199), 68: (0.21853742909113694, 0.6863672034685054, 0.28906788161042285), 583: (0.33249893828748023, 0.5574402721532626, 0.048355320787969336), 584: (0.4417364105098468, 0.4369407216947674, 0.16241194628082245), 76: (0.4655502203943791, 0.10944303345078243, 0.8832444508999896), 79: (0.8823494781169269, 0.8602854575796756, 0.46655973657031047), 84: (0.060221542213292456, 0.01914731167580286, 0.3055281480683151), 85: (0.766342531208258, 0.9245825374766737, 0.37031711910405163), 87: (0.13948591895527063, 0.8844404174150958, 0.20739570597562296), 91: (0.8918452889529781, 0.3489446890522606, 0.5363393265500108), 102: (0.08031539146038547, 0.0017551759017343516, 0.39781039742275426), 119: (0.8606249030204752, 0.006002024038369358, 0.8926479044904958), 632: (0.8107807623400896, 0.3099877573648637, 0.435731436486533), 123: (0.14893028546117915, 0.2517878082271714, 0.9109681753229321), 126: (0.5169187761292617, 0.05239930912138857, 0.13220206501097675), 128: (0.8377118797624784, 0.2403077742096449, 0.75346596060324), 131: (0.39140968224876604, 0.20490073625104321, 0.49724364222766826), 132: (0.15440849286794844, 0.5109256317494821, 0.918663018768346), 134: (0.6802337626345111, 0.3952319177096246, 0.9577912878133846), 136: (0.5429750037107149, 0.2516054077133302, 0.6383395346264112), 140: (0.46426804376009356, 0.5040025154668996, 0.18863898344256602), 144: (0.669049415010293, 0.6601594798409904, 0.3690336138842457), 146: (0.6418660472107188, 0.19387172503903427, 0.08253445229983347), 147: (0.9171177970189475, 0.7570401635513673, 0.41473173765212656), 150: (0.8514416943359722, 0.26776326080817003, 0.42656484426039165), 153: (0.563959718408767, 0.16805776410240414, 0.2368635130939043), 154: (0.6077128018278273, 0.7114298585206303, 0.011655130253268031), 194: (0.9457583531121714, 0.41934982666062404, 0.3692802897910529), 707: (0.19727774650639862, 0.39968360902677436, 0.9650752912041951), 631: (0.7136863081724063, 0.11278804629734518, 0.6916295358238204), 725: (0.006325524188502296, 0.18950234542615196, 0.23926750268622843), 732: (0.5527651291905299, 0.5746966496279889, 0.43171636233396815), 736: (0.5344327591142222, 0.5257392860926776, 0.5651227710291419), 737: (0.7028212878281531, 0.9371346737132197, 0.15804097206531542), 232: (0.31722667708720487, 0.441657298575016, 0.7178566635952561), 240: (0.41580848148241223, 0.04618512467563829, 0.5158900558093626), 249: (0.1150427472614931, 0.05331753045182375, 0.24703683509993657), 272: (0.4470311514274178, 0.6239963553063219, 0.734273183840712), 292: (0.3907724996607741, 0.4380493949515427, 0.5452076825402125), 298: (0.5344828886572797, 0.6263131982198099, 0.8734018104264674), 307: (0.7919826102084409, 0.5608948323741435, 0.8863426580950163), 308: (0.4715901668807123, 0.22691497224040869, 0.8324257857284412), 322: (0.606928934759279, 0.18954053420608696, 0.3971704554820378), 331: (0.43828274661059363, 0.6307222593349302, 0.2340955475172376), 335: (0.3875743287260326, 0.4336592646622611, 0.18786909694048148), 857: (0.6780319762513275, 0.7704555463533739, 0.28812460936085504), 860: (0.5841862317537572, 0.5037085094192894, 0.1285352060375441), 357: (0.4911512658500157, 0.36885328979544607, 0.16493510014450008), 358: (0.1593068931590369, 0.08800651069213683, 0.18999011972464552), 902: (0.26236788359719754, 0.17529748970429215, 0.6484863208369795), 394: (0.02984494188497888, 0.8162917062597478, 0.11484767161474563), 395: (0.06373733176053709, 0.05828579994431693, 0.5276576646723787), 913: (0.2329089726116761, 0.10130531525410325, 0.5097643277292452), 918: (0.3498800067565817, 0.08534208657463194, 0.06750360841059844), 921: (0.8785837493737819, 0.22828450747015672, 0.07405579543608687), 409: (0.7846373211228662, 0.7094511532689909, 0.20386715797977129), 925: (0.115824596742378, 0.34992381657932414, 0.6153763241914337), 932: (0.6128682578052749, 0.25593752365317624, 0.4275747216942438), 933: (0.5665782970092119, 0.22826862385734814, 0.38958016270033535), 936: (0.3984406181611808, 0.06088973642585682, 0.8766893533007929), 942: (0.23548730894370484, 0.5851340605722368, 0.945897539314606), 943: (0.1818978404565259, 0.04768290319210333, 0.892897952279543), 72: (0.7185498068459529, 0.42178934105231114, 0.7170822708612701), 951: (0.2945126748939565, 0.5777632907736129, 0.9200584781435479), 954: (0.24297204338780298, 0.652460465843344, 0.4921529562664547), 957: (0.44375448350658886, 0.9279067963165427, 0.6842608816352503), 961: (0.48137410722891594, 0.09467528600649266, 0.5375593747271779), 963: (0.7023622379209911, 0.17828223889557793, 0.10718503235353127), 966: (0.8259245621037714, 0.42802889162999047, 0.38258746898149265), 970: (0.4945168465360159, 0.40294280549563233, 0.374481199283637), 974: (0.08719382781846197, 0.7675988748519565, 0.8076046247368227), 975: (0.23059187176367324, 0.2657253302615584, 0.3643423610154106), 976: (0.74224238574635, 0.23427758549595035, 0.7699090417859882), 986: (0.09726368948435926, 0.8369969882905206, 0.07986516857033343), 990: (0.9307905999170635, 0.31005065223548134, 0.770015555654754), 991: (0.9289417957628747, 0.21033188329558805, 0.44865447618425736), 992: (0.2694751359724161, 0.45498770799919086, 0.6448059472136883), 993: (0.38997444066817866, 0.9781779063852679, 0.874217562859495), 994: (0.7051477513703358, 0.5702924839652445, 0.24312377606293833), 995: (0.5709641799914025, 0.743539099020067, 0.8261827299024898), 996: (0.8178345478004484, 0.981435239104708, 0.6544046775407857), 997: (0.4320231702054077, 0.07210261858206857, 0.07920415400870395), 998: (0.5627424217341767, 0.1968727734442548, 0.3595950676513303), 999: (0.20981445390600095, 0.30693865142032595, 0.48997043645185046), 1000: (0.9241714458529445, 0.8143896488420276, 0.7663922292951993), 1001: (0.1885301360711723, 0.8389391807577213, 0.0755369071561598), 490: (0.42060664576563456, 0.8132783716104773, 0.07824296338425984)}

outputcolorlist(usz3,already_colored_sizes)