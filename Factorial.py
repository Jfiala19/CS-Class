while True:
	def factorial(number):
		if number == 1:
			return 1
		if number == 900:
			return 67526802209645841583879061361800814224269427869589384312198268703685091643180416969132446952698303794226010370578672908593198347699886928591906501031587651846976759681112609524787093848004428636186893395272784450630354080243217646658024696659065951793757223520229235577548653833681102170973893746054649126415909143150172860721156685810655759230011450132992176454983227538696340112610447029002337004887877266387704586077293585433151612518800147764461182680822867092786694982831838641800997499819339206579415325649748486265233918911087114592440896594062675914294925816719862178374679272092637524786939036290035924271782253738059886933923447877769583003016705363339031413069155837518524761078342052635475632113169618774549275701480106933362990003732589370593557325299434734459295866728988740794174654391479926000848846686708729736713207285203712732201272410830836913052635365082888725171636081587151603468291106754640398232146673627370895934090777828827549554232436190464827998683927179246029919443251026464452337939599198528297828591122689960620361238248313158071643395848405047261412680039877733761849874447323867911712630023171745968278465780558568067035013885275080292137360491875164947724464221693533755035300065350065137490832039523382963747026185653050331832380991844842560750923543775188582096487476950254418365198999674684417286265442786651594404781622946901879166382930714196908227460133027605817864877377712193142137625430353718448269390732615776645283198828602917680224041088993892610506802195917247838900106910698057030379190571057605849323113308634452008179881165616449767648354161225066967961297609698742737923389391615207441152319392845687673311899247085327703421862972871644495409572259985563215471482083325653231777113271326579970310755604973969708949477374254974480294652427022436705380184064008853457214518515270985563195412993145274057688634448812449445800617631162768243125606424844709372022149908463572254912654907763445758543980999149122998104378965626781898655221443263601405152073199706585080288735040205417371277253096243200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
		return number*factorial(number -1)
	x = int(input("Enter #\n\n>>"))
	print(factorial(x))