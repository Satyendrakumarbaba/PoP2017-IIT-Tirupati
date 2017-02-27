from termcolor import colored
import math,string
d={}
def assign(text):
    key=text[:text.index('=')]
    text=text[text.index('=')+1:]
    if(len(text)==0):
        print colored('[out]->', 'red'),colored("Error there is nothing to assign",'red')
    else:
        if '"' in text:
            d[key]=text
        else:
            try:
                d[key]=int(text)
            except:
                d[key]=d[text]
def interpreter(text,flag):
    sym=1
    count=0
    left=0
    if flag==1:
        if text[0] == '-':
            sym=-1
        text=text[1:]
    for i in text:
        try:
            left=left*10+float(i)
            count=count+1
        except:
            break
    if count>0:
        right=0
        f=0
        index=count+1
        for i in range(index,len(text)):
            try:
                right=right*10+float(text[i])
                f=f+1
            except:
                break
        left=left*sym
        if f>0:
            if text[count]=='+':
                print colored('[out]', 'red'), left+right
            elif text[count]=='-':
                print colored('[out]', 'red'),left-right
            elif text[count]=='*':
                print colored('[out]', 'red'),left*right
            elif text[count]=='/':
                print colored('[out]', 'red'),left/right
            elif text[count]=='%':
                print colored('[out]', 'red'),left%right
            elif text[count]=='^':
                print colored('[out]', 'red'),left**right
            else:
                print colored('[out]', 'red'),"Invalid input see the middle"
        else:
            print colored('[out]', 'red'),"Invalid input see the ending"
    else:
        print colored('[out]', 'red'),"Invalid input see the starting"
def calulation(command):
                    c=command
                    a=command
		    k=0
                    for i in range(0,len(a)):
			if k>len(a)-1:
				      break
                        tmp=a[k]
                        if("+" in tmp) or ("-" in tmp) or ("*" in tmp) or ("/" in tmp) or ("%" in tmp) or ("^" in tmp):
                            k=k+1
                        else:
                            try:
                                float(tmp)
			    	k=k+1
                            except:
                                tmp_s=a[k]
                                for j in range(k+1,len(a)) :
                                       if (a[j]=="+") or (a[j]=="-") or (a[j]=="*") or (a[j]=="/") or (a[j]=="%") or (a[j]=="^"):
                                        k=j+1
                                        break
                                       else:
                                        tmp_s=tmp_s+a[j]
                                        k=j+1
				print tmp_s,k
                                c=string.replace(c, tmp_s, str(d[tmp_s]))
                    return eval(c)
def main(text):
    if '=' in text:
        assign(text)
    elif('display' in text):
        text=text[7:]
        try:
            print colored('[out]', 'red'), d[text]
        except:
            print colored(text,'red'),colored("is not defined",'red')
    elif('for' in text):
        commands=[]
        while True:
            count=0
            commands.append((raw_input(colored("----->",'blue')).replace(" ","")).replace("\t",""))
            if commands[len(commands)-1]=='end' or commands[len(commands)-1]=='\tend':
                commands.remove('end')
                break
            elif commands[len(commands)-1]=='':
                count=count+1
                if count>=2:
                    print colored('Error: Please enter end to END the loop')
        start=0
        end=0
        index=text.index('(')
        for i in range(index+1,len(text)):
            try:
                start=start*10+int(text[i])
            except:
                index=i
                break
        for i in range(index+1,len(text)):
            try:
                end=end*10+int(text[i])
            except:
                index=i
                break
        increment=0
        for i in range(index+1,len(text)):
            try:
                increment=increment*10+int(text[i])
            except:
                index=i+1
                break
        if increment == 0:
            increment=1
        for i in range(start,end,increment):
            d['i']=i
            for command in commands:
                command=command.replace(" ","")
                if '=' in command:
                    if("+" in command) or ("-" in command) or ("*" in command) or ("/" in command) or ("%" in command) or ("^" in command):
                        key=command[:command.index('=')]
                        text=command[command.index('=')+1:]
                        text=float(calulation(text))
                        d[key]=text
                    else:
                        assign(command)
                elif ("+" in command) or ("-" in command) or ("*" in command) or ("/" in command) or ("%" in command) or ("^" in command):
                    print calulation(command)
                elif 'display' in command:
                    text=command[7:]
                    try:
                        print colored('[out]', 'red'), d[text]
                    except:
                        print colored(text,'red'),colored("is not defined",'red')            
    else:
        try:
            d[text]+1 
            print colored('[out]', 'red'), d[text]
        except:
                print calulation(text)
while True:    
    text=raw_input(colored('[In]->','blue'))
    text = text.replace(" ", "")
    main(text)
