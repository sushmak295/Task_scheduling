import operator
import sys
filename = sys.argv[-1]
c=0
b=0
combination=[]
file1=open(filename,'r')
content=[]
d={}
tasks={}
#calculating numebr of lines in the file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

length=file_len(filename)

#taking input from file
with open(filename) as f:
    for i in range(1,length):
            tasks[i]={}
    
    for j in range(0,length):
        content = f.readline()  
        line=content.split(' ')
        #reading general values
        
        if j==0:
            d["#_of_tasks"]=int(line[0])
            d["tot_exe_tym"]=int(line[1])
            d["p@1188"]=int(line[2])
            d["p@918"]=int(line[3])
            d["p@648"]=int(line[4])
            d["p@384"]=int(line[5])
            d["p@lowfreq"]=str(line[6])
            d["p@lowfreq"]=int(d["p@lowfreq"].replace('\n',''))
        #reading values for each task
        
        for k in range(1,length):
            if k==j:
                tasks[j]['name']=line[0]
                tasks[j]['period']=int(line[1])
                tasks[j]['wcet@1188']=int(line[2])
                tasks[j]['wcet@918']=int(line[3])
                tasks[j]['wcet@648']=int(line[4])
                line[5]=str(line[5])
                tasks[j]['wcet@384']=line[5].replace('\n','')
                tasks[j]['wcet@384']=int(tasks[j]['wcet@384'])
dynamic=[]
for k in range(1,length):
    dynamic.append({'name':tasks[k]['name'],'period':tasks[k]['period'],0:tasks[k]['wcet@1188'],1:tasks[k]['wcet@918'],2:tasks[k]['wcet@648'],3:tasks[k]['wcet@384']})

print dynamic    



frequency={0:1188,1:918,2:648,3:348}

energy={0:d["p@1188"]/float(1000),1:d["p@918"]/float(1000),2:d["p@648"]/float(1000),3:d["p@384"]/float(1000)}
e=0.0
totener=0.0
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            for l in range(0,4):
                for m in range(0,4):
                    #for g in range(1,length):
                    e=(float(dynamic[0][i])/float(dynamic[0]['period']))+(float(dynamic[1][j])/float(dynamic[1]['period']))+(float(dynamic[2][k])/float(dynamic[2]['period']))+(float(dynamic[3][l])/float(dynamic[3]['period']))+(float(dynamic[4][m])/float(dynamic[4]['period']))
                    #print e
                    #print i,j,k,l,m,"end"
                    
                    b=b+1
                    if e<1:
                        #print i,j,k,l,m,"end"
                        #print e
                        totener=(dynamic[0][i]*(energy[i]))+(dynamic[1][j]*(energy[j]))+(dynamic[2][k]*(energy[k]))+(dynamic[3][l]*(energy[l]))+(dynamic[4][m]*(energy[m]))
                        c=c+1
                        combination.append({'w1 at':frequency[i],'w2 at':frequency[j],'w3 at':frequency[k],'w4 at':frequency[l],'w5 at':frequency[m],'w1exetym':dynamic[0][i],'w2exetym':dynamic[1][j],'w3exetym':dynamic[2][k],'w4exetym':dynamic[3][l],'w5exetym':dynamic[4][m],'totalenergy':totener})
                        #print i,j,k,l,m,"end"
print "total number of combinations:",b
print "possible combinatioins:",c

combination.sort(key=operator.itemgetter('totalenergy'))

print "best combination:",combination[0]['totalenergy']
lists=[]
tasks={1:{'id':'1','name':'w1','period':tasks[1]['period'],'deadline':tasks[1]['period'],'exetym':combination[0]['w1exetym'],'remexetym':combination[0]['w1exetym'],'frequency':combination[0]['w1 at']},
       2:{'id':'2','name':'w2','period':tasks[2]['period'],'deadline':tasks[2]['period'],'exetym':combination[0]['w2exetym'],'remexetym':combination[0]['w2exetym'],'frequency':combination[0]['w2 at']},
       3:{'id':'3','name':'w3','period':tasks[3]['period'],'deadline':tasks[3]['period'],'exetym':combination[0]['w3exetym'],'remexetym':combination[0]['w3exetym'],'frequency':combination[0]['w3 at']},
       4:{'id':'4','name':'w4','period':tasks[4]['period'],'deadline':tasks[4]['period'],'exetym':combination[0]['w4exetym'],'remexetym':combination[0]['w4exetym'],'frequency':combination[0]['w4 at']},
       5:{'id':'5','name':'w5','period':tasks[5]['period'],'deadline':tasks[5]['period'],'exetym':combination[0]['w5exetym'],'remexetym':combination[0]['w5exetym'],'frequency':combination[0]['w5 at']}}
idle={'name':'IDLE'}
a=[]




power={1188:0.625,918:0.447,648:0.307,348:0.212}

def edf(i):
    
    if i==0:
        for j in range(1,6):
            lists.append(tasks[j])
    for j in range(1,6):
        tasks[j]['deadline']=tasks[j]['deadline']-1
        if (i % tasks[j]['period']==0 and i!=0):
            tasks[j]['deadline']=tasks[j]['deadline']+tasks[j]['period']
            tasks[j]['remexetym']=tasks[j]['exetym']
            lists.append(tasks[j])
   
    if len(lists)!=0:
        lists.sort(key=operator.itemgetter('deadline'))
        a.append(lists[0])
        #print (i,":",lists[0]['name'])#,':',lists[0]['start'],':',lists[0]['end'])
        #executing.append(lists[0]['name'])
        if lists[0]['remexetym']>0:
            lists[0]['remexetym']=lists[0]['remexetym']-1
                     
            if lists[0]['remexetym']==0:
                
                lists.remove(lists[0])
        
    else:
        a.append(idle)
    
   
#print executing    
        
   
print "start task end  frequency  energy"            
for k in range(0,1000):    

     edf(k)
total=0
idl=0
total_w1=0
total_w2=0
total_w3=0
total_w4=0
total_w5=0

for t in range(0,len(a)):
            k=t+1
            if t==0:
                start=0
            if k!=len(a):
                if a[t]['name']!=a[k]['name']:
                    end=t+1
                    if a[t]['name']!='IDLE':
                    
                        total=total+(end-start)*power[a[t]['frequency']]
                        print " ",start,"  ",a[t]['name']," ",end,"  ",a[t]['frequency'],"  ",(end-start)*power[a[t]['frequency']]
                        if a[t]['name']=='w1':
                            total_w1=total_w1+(end-start)
                        if a[t]['name']=='w2':
                            total_w2=total_w2+(end-start)
                        if a[t]['name']=='w3':
                            total_w3=total_w3+(end-start)
                        if a[t]['name']=='w4':
                            total_w4=total_w4+(end-start)
                        if a[t]['name']=='w5':
                            total_w5=total_w5+end-start
                        
                        
                    else:
                        idl=idl+end-start
                        total=total+(end-start)*.84
                        print " ",start,"  ",a[t]['name']," ",end,"  ","IDLE","  ",(end-start)*.84
                    start=t+1
            if k==len(a):
                if a[t]['name']!='IDLE':
                    
                        total=total+(len(a)-start)*power[a[t]['frequency']]
                        print " ",start,"  ",a[t]['name']," ",len(a),"  ",a[t]['frequency'],"  ",(len(a)-start)*power[a[t]['frequency']]
                        if a[t]['name']=='w1':
                            total_w1=total_w1+(len(a)-start)
                        if a[t]['name']=='w2':
                            total_w2=total_w2+(len(a)-start)
                        if a[t]['name']=='w3':
                            total_w3=total_w3+(len(a)-start)
                        if a[t]['name']=='w4':
                            total_w4=total_w4+(len(a)-start)
                        if a[t]['name']=='w5':
                            total_w5=total_w5+len(a)-start
                        
                        
                else:
                        idl=idl+end-start
                        total=total+(len(a)-start)*.84
                        print " ",start,"  ",a[t]['name']," ",end,"  ","IDLE","  ",(len(a)-start)*.84
print "total energy:",total
print "idle percent:",idl/float(10)
print "w1 executes totally for:",total_w1
print "w2 executes totally for:",total_w2
print "w3 executes totally for:",total_w3
print "w4 executes totally for:",total_w4
print "w5 executes totally for:",total_w5

