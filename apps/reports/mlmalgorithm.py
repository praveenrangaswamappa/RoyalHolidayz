from RoyalHolidayz.models import Candidate, Sponsorer

class MLM:
	"""class for solving MLM"""
	def __init__(self):
		"""constructor for MLM"""
		self.listoftuples = []
		self.createbinarytree()
		self.allundercandidate = []
		self.pair = 0
		self.firstleftchild = None
		self.firstrightchild = None
		#self.children = []

	def createbinarytree(self):
		"""creates binary tree using list of tuples"""
		obj = Sponsorer.objects.all()
		for item in obj:
		     self.listoftuples.append((item.candidateid,item.sponsorid, item.leg))

	def checknodes(self, candidate):
	    	"""count number of pairs for a candidate and display points"""
		count = 0
	    	
		tempcandidate = candidate
		#print "*******checking for childrens of %s*****"%candidate
		
		#*********to get first left and right child*************
#		if not self.firstleftchild and self.firstrightchild:
		for item in self.listoftuples:
			tempsponsorer = u"%s"%item[1]
			
			if ((tempsponsorer == candidate)and ("%s"%item[0] != "%s"%item[1])):
				if not self.firstleftchild  and u"%s"%item[2] == "L":
					print self.firstleftchild
					self.firstleftchild = item[0]
				if not self.firstrightchild  and u"%s"%item[2] == "R":
					print self.firstrightchild
					self.firstrightchild = item[0]
	    	
	    	def countpair(candidate):
			
			self.candidateslist = []
			templist = []
			for item in self.listoftuples:
				tempsponsorer = u"%s"%item[1]
				
				if ((tempsponsorer == candidate)and ("%s"%item[0] != "%s"%item[1])):
			   		
			   		#print "candidate %s sponsorer = %s"%(item[0], item[1])
			   			
			   		self.candidateslist.append(u"%s"%item[0])
					self.allundercandidate.append((u"%s"%item[0],u"%s"%item[2],u"%s"%item[1]))
					
			   		#print "current list of children",self.candidateslist
					#print "current list of all under candidate",self.allundercandidate
			   		if len(self.candidateslist) == 2:
			   			self.pair = self.pair + 1
						#print "total number of pairs found %d"%self.pair		
			
				tempcandidate = None
			
			if self.candidateslist:		
	    			for candidates in self.candidateslist:
					#print "*******checking for childrens of %s*****"%candidates
					countpair(candidates)
		
				
		
		if tempcandidate:
			countpair(candidate)
			
		
		
		return (self.allundercandidate, self.pair, len(self.allundercandidate))
	    
	
	def start(self, candidate):
#		self.display()
		listofallunderlefcandidate, numberofpairs, totalnumberofchilds = self.checknodes(candidate)
#		print "total number of candidates under %s are =  %d"%(candidate, len(self.allundercandidate))
		
		print "number of pairs=%d, total amount to be awarded = %d, total number of childs = %d"%(numberofpairs, (numberofpairs *1000), totalnumberofchilds)
		print "list of all under candidate = ",listofallunderlefcandidate
		
		print "-------------------The End------------------"

	def printfirstleftrightchilds(self):
		print "first left child = %s"%self.firstleftchild
		print "first right child = %s"%self.firstrightchild
		
	def calculatepoints(self, count):
		if count >= 2:
			print "found 1 pair"

	def display(self):
		"""displays candidate and sponsorer"""
		print self.listoftuples
		count = 0
		for item in self.listoftuples:
		    print "candidate %s sponsorer = %s"%(item[0], item[1])
		    
		    

	def __del__(self):
		pass

#obj = MLM()
#obj.display()
#obj.start("Praveen")
#obj.printfirstleftrightchilds()
#
#obj.pair = 0
#obj.allundercandidate = []
#obj.start(u"%s"%obj.firstleftchild)
#
#obj.pair = 0
#obj.allundercandidate = []
#obj.start(u"%s"%obj.firstrightchild)


