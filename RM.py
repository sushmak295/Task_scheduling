
import operator
import sys
filename = sys.argv[-1]

lists=[]
executing=[]

final=[]
file=open(filename,'r')
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
                tasks[j]['deadline']=tasks[j]['period']
                tasks[j]['wcet@1188']=int(line[2])
                tasks[j]['exetym']=tasks[j]['wcet@1188']
                tasks[j]['remexetym']=tasks[j]['wcet@1188']              
                tasks[j]['wcet@918']=int(line[3])
                tasks[j]['wcet@648']=int(line[4])
                line[5]=str(line[5])
                tasks[j]['wcet@384']=line[5].replace('\n','')
                tasks[j]['wcet@384']=int(tasks[j]['wcet@384'])




           
        
      
        
        
        
        

idle={'name':'IDLE'}
a=[] 

def RM(i):
    
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
        executing.append(lists[0]['name'])
        if lists[0]['remexetym']>0:
            lists[0]['remexetym']=lists[0]['remexetym']-1
                     
            if lists[0]['remexetym']==0:
                
                lists.remove(lists[0])
        
    else:
        a.append(idle)
    
freq_task=1188
freq_idle=384
power_task=d["p@1188"]/float( d["tot_exe_tym"])
power_idle=d["p@lowfreq"]/float( d["tot_exe_tym"])     
#print executing
exp=1/float(d["#_of_tasks"])
rrm=d["#_of_tasks"]*(2**exp-1)
lrm=tasks[1]['exetym']/float(tasks[1]['period'])+tasks[2]['exetym']/float(tasks[2]['period'])+tasks[3]['exetym']/float(tasks[3]['period'])+tasks[4]['exetym']/float(tasks[4]['period'])+tasks[5]['exetym']/float(tasks[5]['period'])   
if lrm<=rrm:
    idl=0
    print "start task end"            
    for k in range(0,1000):

         RM(k)
    total_w1=0
    total_w2=0
    total_w3=0
    total_w4=0
    total_w5=0

    for t in range(0,len(a)):
        k=t+1
        if t==0:
            start=0
            total=0
        if k!=len(a):   
            if a[t]['name']!=a[k]['name']:
                end=t+1
                if a[t]['name']!='IDLE':
                    total=total+(end-start)*power_task
                    print " ",start,"  ",a[t]['name']," ",end,"  ",freq_task,"  ",(end-start)*power_task
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
                    total=total+(end-start)*power_idle
                    
                    
                    print " ",start,"  ",a[t]['name']," ",end,"  ","IDLE","  ",(end-start)*power_idle
                start=t+1
        if k==len(a):
            if a[t]['name']!='IDLE':
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
                            #print total_w5
                
                total=total+(len(a)-start)*power_task
                print " ",start,"  ",a[t]['name']," ",len(a),"  ",freq_task,"  ",(len(a)-start)*power_task
            else:
                idl=idl+len(a)-start
                total=total+(len(a)-start)*power_idle
                print " ",start,"  ",a[t]['name']," ",len(a),"  ","IDLE","  ",(len(a)-start)*power_idle
    print "total energy:",total
    print "idle percent:",idl/float(10)
    print "w1:",total_w1
    print "w2:",total_w2
    print "w3:",total_w3
    print "w4:",total_w4
    print "w5:",total_w5
    
else:
    #print exp
    #print rrm
    print "Rate Monotonic Scheduling can not be achieved" 

     
    
            
            
        
        








       
