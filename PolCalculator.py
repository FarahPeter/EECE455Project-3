import tkinter as tk
import galois

#for error messages
def popupmsg(msg,tit="Warning!",size="300x80"):

    popup = tk.Tk()
    popup.geometry(size)
    popup.wm_title(tit)
    label = tk.Label(popup, text=msg, font="NORM_FONT")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#to display final result
def updateresult(msg,r=0):
    if (len(msg)<65):
        FlabelD['text']=(msg)
    else:
        FlabelD['text']="Too large to display properly"
    if (r==0):
        i=0
        dec=""
        for ss in msg:
            if(i<3):
                i=i+1
            else:
                if(ss!=','):
                    dec=dec+ss
                else:
                    break
        dec=int(dec)   
        finalsb=str(bin(dec))
        finalsh=str(hex(dec))
        if (len(finalsb)<65):
            FlabelB['text']=(finalsb)
        else:
            FlabelB['text']="Too large to display properly"
        
        FlabelH['text']=(finalsh)
    else:
        dec=int(msg)
        finalsb=str(bin(dec))
        finalsh=str(hex(dec))
        if (len(finalsb)<65):
            FlabelB['text']=(finalsb)
        else:
            FlabelB['text']="Too large to display properly"
        
        FlabelH['text']=(finalsh)
        







def reduce(a,GFf,w=-1):
    
    
    # G = galois.GF(2**int(gf.get()))
    # gg=str((G.irreducible_poly))
    
    GFf=2 ** (int(GFf))
    P= galois.GF(GFf)
    pp=str((P.irreducible_poly))
    re=""
    begincompy=0
    for st in pp:
        if (st==','):
            break
        if (begincompy==1):
            re=re+st
        elif (begincompy==0):
            if (st=='('):
                begincompy=1
    expo=[] #array containing value of exponents that have coef=1 not 0
    List=re.split("+")
    for ele in List:
        if('^' in ele):
            temp=ele.split("^")
            expo.append(temp[1])
        elif('x' in ele):
            expo.append('1')
        elif('1' in ele):
            expo.append('0')

    decred=0 #decimal value of irredusable polinomiale
    for i in range (len(expo)):
         decred=decred+2**(int(expo[i]))
    
    q=a//decred
    bbb=a-q*decred
    if (bbb>=GFf):
        bbb=decred-bbb
    if (w==-1):
        return bbb
    else:
        updateresult(str(bbb),1)
    






def add(a,b,GF):
    t=GF
    GF=2 ** (int(GF))
    if(a>=GF):
        a=reduce(a,t)
    if(b>=GF):
        b=reduce(b,t)

    gp = galois.GF(GF)
    x=gp(a)
    y=gp(b)
    z=x+y
    updateresult(str(z))

    
 
    
def sub(a,b,GF):
    t=GF
    GF=2 ** (int(GF))
    if(a>=GF):
        a=reduce(a,t)
        print(a)
    if(b>=GF):
        b=reduce(b,t)
        print(b)
        
    gp = galois.GF(GF)   
    x=gp(a)
    y=gp(b)
    z=x-y
    updateresult(str(z))
    
def mul(a,b,GF):
    t=GF
    GF=2 ** (int(GF))
    if(a>=GF):
        a=reduce(a,t)
    if(b>=GF):
        b=reduce(b,t)

    gp = galois.GF(GF)
    x=gp(a)
    y=gp(b)
    z=x*y
    updateresult(str(z))

def div(a,b,GF):
    t=GF
    GF=2 ** (int(GF))
    if(a>=GF):
        a=reduce(a,t)
    if(b>=GF):
        b=reduce(b,t)

    gp = galois.GF(GF)  
    x=gp(a)
    y=gp(b)
    z=x/y
    updateresult(str(z))

def inv(a,GF):
    t=GF
    GF=2 ** (int(GF))
    if(a>=GF):
        a=reduce(a,t)
    gp = galois.GF(GF)  
    z=gp(1)/gp(a)
    updateresult(str(z))

def check(whatdo,Ba,Bb,Ha,Hb,GF):
    PH=-1 #if PH=0 using binary input if PH=1 using HEX input
    LBa=len(Ba)
    LBb=len(Bb)
    LHa=len(Ha)
    LHb=len(Hb)
    LGF=len(GF)
    if (LGF==0):
        popupmsg("Spesify galois field to work on")
    if (LBa!=0):
        for st in (Ba):
            if (st!='0' and st!='1'):
                popupmsg("Bin1 invalid input")
    
    if (LBb!=0):
        for st in (Bb):
            if (st!='0' and st!='1'):
                popupmsg("Bin2 invalid input")
            
    if (LHa!=0):
        for st in (Ha):
            if (st!='0' and st!='1' and st!='2' and st!='3' and st!='4' and st!='5' and st!='6' and st!='7' and st!='8' and st!='9' and st!='a' and st!='b' and st!='c' and st!='d' and st!='e' and st!='f' and st!='A' and st!='B' and st!='C' and st!='D' and st!='E' and st!='F'):
                popupmsg("Hex1 invalid input")

    if (LHb!=0):
        for st in (Hb):
            if (st!='0' and st!='1' and st!='2' and st!='3' and st!='4' and st!='5' and st!='6' and st!='7' and st!='8' and st!='9' and st!='a' and st!='b' and st!='c' and st!='d' and st!='e' and st!='f' and st!='A' and st!='B' and st!='C' and st!='D' and st!='E' and st!='F'):
                popupmsg("Hex2 invalid input")

    if ((LBa!=0 or LBb!=0) and (LHa!=0 or LHb!=0)):
        popupmsg("Shoose only HEX or BIN option")
    
    
    if (int(GF)>139):
        popup = tk.Tk()
        popup.geometry("300x80")
        popup.wm_title("Warning!")
        label = tk.Label(popup, text=("2^"+str(GF)+" is large and may take a long time"), font="NORM_FONT", fg="red")
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="OK", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    
    
    try:
        G = galois.GF(2**int(gf.get()))
        gg=str((G.irreducible_poly))
        if (len(gg)<150):
            la['text']=(gg)
        else:
            la.config(text="Can not display Polinomial")
    except:
        la.config(text=("No Irredusable Polinomial in GF 2^"+ str(GF)))
        popupmsg("No Irredusable Polinomial in GF 2^"+ str(GF))
    
    
    if (whatdo==4):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to inverte")
        if (LBa !=0):
            if (LBb!=0 or LHa!=0 or LHb!=0):
                popupmsg("Inv only needs one argument")
        if (LBb !=0):
            if (LBa!=0 or LHa!=0 or LHb!=0):
                popupmsg("Inv only needs one argument")
        if (LHa !=0):
            if (LBb!=0 or LBa!=0 or LHb!=0):
                popupmsg("Inv only needs one argument")
        if (LHb !=0):
            if (LBb!=0 or LHa!=0 or LBa!=0):
                popupmsg("Inv only needs one argument")
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa!=0):
                ans=int(Ba, 2)
                inv(ans,GF)
            else:
                ans=int(Bb, 2)
                inv(ans,GF)
        if (LHa!=0 or LHb!=0):
            PH=1
            if (LHa!=0):
                ans=int(Ha, 16)
                inv(ans,GF)
            else:
                ans=int(Hb, 16)
                inv(ans,GF)
    
  
    
  
    if (whatdo==5):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to Reduce")
        if (LBa !=0):
            if (LBb!=0 or LHa!=0 or LHb!=0):
                popupmsg("Reduce only needs one argument")
        if (LBb !=0):
            if (LBa!=0 or LHa!=0 or LHb!=0):
                popupmsg("Reduce only needs one argument")
        if (LHa !=0):
            if (LBb!=0 or LBa!=0 or LHb!=0):
                popupmsg("Reduce only needs one argument")
        if (LHb !=0):
            if (LBb!=0 or LHa!=0 or LBa!=0):
                popupmsg("Reduce only needs one argument")
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa!=0):
                ans=int(Ba, 2)
                reduce(ans,GF,whatdo)
            else:
                ans=int(Bb, 2)
                reduce(ans,GF,whatdo)
        if (LHa!=0 or LHb!=0):
            PH=1
            if (LHa!=0):
                ans=int(Ha, 16)
                reduce(ans,GF,whatdo)
            else:
                ans=int(Hb, 16)
                reduce(ans,GF,whatdo)
    
    
    if (whatdo==0):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to Add")
        #check bin or hex and check if both argument are given then pass throw to apropriate function
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa==0 or LBb==0):
                 popupmsg("Add takes 2 arguments")
        elif(LHa!=0 or LHb!=0):
            PH=1
            if (LHa==0 or LHb==0):
                 popupmsg("Add takes 2 arguments")
                 
        if (PH==0):
            ans1=int(Ba, 2)
            ans2=int(Bb, 2)
            add(ans1,ans2,GF)
        elif (PH==1):
            ans1=int(Ha, 16)
            ans2=int(Hb, 16)
            add(ans1,ans2,GF)
        
    if (whatdo==1):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to Substracte")
        #check bin or hex and check if both argument are given then pass throw to apropriate function
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa==0 or LBb==0):
                 popupmsg("Substracte takes 2 arguments")
        elif(LHa!=0 or LHb!=0):
            PH=1
            if (LHa==0 or LHb==0):
                 popupmsg("Substracte takes 2 arguments")
                 
        if (PH==0):
            ans1=int(Ba, 2)
            ans2=int(Bb, 2)
            sub(ans1,ans2,GF)
        elif (PH==1):
            ans1=int(Ha, 16)
            ans2=int(Hb, 16)
            sub(ans1,ans2,GF)
    
    if (whatdo==2):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to Multiply")
        #check bin or hex and check if both argument are given then pass throw to apropriate function
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa==0 or LBb==0):
                 popupmsg("Multiply takes 2 arguments")
        elif(LHa!=0 or LHb!=0):
            PH=1
            if (LHa==0 or LHb==0):
                 popupmsg("Multiply takes 2 arguments")
        
        if (PH==0):
            ans1=int(Ba, 2)
            ans2=int(Bb, 2)
            mul(ans1,ans2,GF)
        elif (PH==1):
            ans1=int(Ha, 16)
            ans2=int(Hb, 16)
            mul(ans1,ans2,GF)
    
    if (whatdo==3):
        if (LBa==0 and LBb==0 and LHa==0 and LHb==0):
            popupmsg("Nothing to Divide")
        #check bin or hex and check if both argument are given then pass throw to apropriate function
        if (LBa!=0 or LBb!=0):
            PH=0
            if (LBa==0 or LBb==0):
                 popupmsg("Divide takes 2 arguments")
        elif(LHa!=0 or LHb!=0):
            PH=1
            if (LHa==0 or LHb==0):
                 popupmsg("Divide takes 2 arguments")

        if (PH==0):
            ans1=int(Ba, 2)
            ans2=int(Bb, 2)
            div(ans1,ans2,GF)
        elif (PH==1):
            ans1=int(Ha, 16)
            ans2=int(Hb, 16)
            div(ans1,ans2,GF)
        





master = tk.Tk()
master.wm_title("Polinomiale calculator")
master.geometry("1200x400")

tk.Label(master, text="Polynomial1 in binary").grid(row=0, column=1,ipadx=200)
tk.Label(master, text="Polynomial2 in binary").grid(row=1, column=1,ipadx=200)
tk.Label(master, text="Polynomial1 in HEX").grid(row=2, column=1,ipadx=200)
tk.Label(master, text="Polynomial2 in HEX").grid(row=3, column=1,ipadx=200)
tk.Label(master, text="GF(2^m); m=").grid(row=4, column=1,ipadx=200)
tk.Label(master, text="Result in Decimal:",bg="red").grid(row=5, column=1,ipadx=200)
tk.Label(master, text="Result in Binary:",bg="green").grid(row=6, column=1,ipadx=200)
tk.Label(master, text="Result in Hexadecimal:",bg="#0000FF").grid(row=7, column=1,ipadx=200)


polBin1 = tk.Entry(master)
polBin2 = tk.Entry(master)
polHex1 = tk.Entry(master)
polHex2 = tk.Entry(master)
gf = tk.Entry(master)

polBin1.grid(row=0, column=2)
polBin2.grid(row=1, column=2)
polHex1.grid(row=2, column=2)
polHex2.grid(row=3, column=2)
gf.grid(row=4,column=2)


la=tk.Label(master, text="",fg="black", pady=10, padx=10, font=10)
la.grid(row=9, column=2,ipadx=0)
tk.Label(master, text="Iredusable Polinomiale:",fg="black").grid(row=9, column=1,ipadx=0)




addi=tk.Button(master,text="Add",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(0,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
addi.grid (row=0,column=0)

subs=tk.Button(master,text="Sub",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(1,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
subs.grid (row=1,column=0)

mult=tk.Button(master,text="Mul",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(2,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
mult.grid (row=2,column=0)

divi=tk.Button(master,text="Div",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(3,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
divi.grid (row=3,column=0)

invr=tk.Button(master,text="Inv",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(4,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
invr.grid (row=4,column=0)

redu=tk.Button(master,text="Red",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: check(5,polBin1.get(),polBin2.get(),polHex1.get(),polHex2.get(),gf.get()))
redu.grid (row=5,column=0)

abo=tk.Button(master,text="About",padx=20,pady=5,fg="black",bg="#263D42",command=lambda: popupmsg("Develloped by Peter Farah, Anthony Saab, and Karim Ghadar for EECE455 project#3","About","600x80"))
abo.grid (row=6,column=0)

FlabelD =tk.Label(master,text="",fg="black",bg="red",pady=10, padx=10, font=10)
FlabelD.grid(row=5,column=2)
FlabelB =tk.Label(master,text="",fg="black",bg="green",pady=10, padx=10, font=10)
FlabelB.grid(row=6,column=2)
FlabelH =tk.Label(master,text="",fg="black",bg="#0000FF",pady=10, padx=10, font=10)
FlabelH.grid(row=7,column=2)


master.mainloop()
