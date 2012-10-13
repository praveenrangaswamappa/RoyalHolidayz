# Create your views here.

from apps.reports.mlmalgorithm import MLM
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse

def candidatereport(request):
    objMLM = MLM()
    #obj.display()
    listofallunderleftcandidate, numberofpairs, totalnumberofchilds = objMLM.checknodes("Praveen 2")
    objMLM.printfirstleftrightchilds()
    objMLM.pair = 0; objMLM.allundercandidate = []
    temprightlist, numberofleftpairs, totalnumberofchildstowardsleft = objMLM.checknodes(u"%s"%objMLM.firstleftchild)
    objMLM.pair = 0; objMLM.allundercandidate = []
    templeftlist, numberofrightpairs, totalnumberofchildstowardsright= objMLM.checknodes(u"%s"%objMLM.firstrightchild)
    
    
    return render_to_response("base.html",{"listofallunderleftcandidate":listofallunderleftcandidate[0:2],
                                            "numberofpairs":numberofpairs, 
                                            "totalnumberofchilds":totalnumberofchilds,
                                            "templeftlist":templeftlist[0:2],
                                            "numberofleftpairs":numberofleftpairs, 
                                            "totalnumberofchildstowardsleft":(totalnumberofchildstowardsleft + 1),
                                            "temprightlist":temprightlist[0:2],
                                           "numberofrightpairs":numberofrightpairs, 
                                           "totalnumberofchildstowardsright":(totalnumberofchildstowardsright + 1)}, 
                              context_instance=RequestContext(request))
    
