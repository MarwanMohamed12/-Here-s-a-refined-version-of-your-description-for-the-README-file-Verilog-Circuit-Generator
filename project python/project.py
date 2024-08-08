# here is function to check keywords
def name_check(name,list_t):
    reserved_keywords =[
    "always", "and", "assign", "automatic", "begin", "buf", "bufif0", "bufif1",
    "case", "casex", "casez", "cell", "cmos", "config", "deassign", "default",
    "defparam", "design", "disable", "edge", "else", "end", "endcase", "endconfig",
    "endfunction", "endmodule", "endprimitive", "endspecify", "endtable", "endtask",
    "event", "for", "force", "forever", "fork", "function", "generate", "genvar",
    "highz0", "highz1", "if", "ifnone", "incdir", "include", "initial", "inout",
    "input", "instance", "integer", "join", "large", "liblist", "library", "localparam",
    "macromodule", "medium", "module", "nand", "negedge", "nmos", "nor", "noshowcancelled",
    "not", "notif0", "notif1", "or", "output", "parameter", "pmos", "posedge", "primitive",
    "pull0", "pull1", "pulldown", "pullup", "pulsestyle_onevent", "pulsestyle_ondetect",
    "rcmos", "real", "realtime", "reg", "release", "repeat", "rnmos", "rpmos", "rtran",
    "rtranif0", "rtranif1", "scalared", "showcancelled", "signed", "small", "specify",
    "specparam", "strong0", "strong1", "supply0", "supply1", "table", "task", "time",
    "tran", "tranif0", "tranif1", "tri", "tri0", "tri1", "triand", "trior", "trireg",
    "unsigned", "use", "vectored", "wait", "wand", "weak0", "weak1", "while", "wire",
    "wor","xnor","xor"]
    reserved_special = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}',
                        '[', ']', '|', ':', ';', "'", '"', '`', '<', '>', ',', '.', '?', '/',' ','$']
    
    
    for i in reserved_special:
        if name.find(i)>=0:
            check2= 0
            print("there is special character\n")
            break
        else :
            check2= 1
        
    for i in reserved_keywords:
        if name.lower()==i:
            check1 = 0
            print("there is special there is special keyword\n")
            break
        else :
            check1= 1
    for i in list_t:
        if name.lower()==i:
            check4 = 0
            print("this name is repeated\n")
            break
        else :
            check4= 1
            
    if(name[0].isdigit()):
        check3=0
        print("there is digit in first character\n")
    else:
        check3=1
        
        
    return check1 and check2 and check3 and check4

#check for choice
def check_for_booliain(num):
    while num >1:
        num=int(input("enter right choice 1 or 0\n"))
    
    
    return num
#check if parameter is found or not
def para_check(parameter_List,parameter_Check):
     while  not(parameter_Check in parameter_List):
         parameter_Check=input("this parameter isnt in list try again\n")
     return parameter_Check
    
def check_for_syn(num2):
     while num2 <1 or num2 >4:
         num2=int(input("enter right choice 1 or 2 or 3 or 4\n"))
     return num2
   
########################################

in_out=[] #we initialize inputs and output to use in Tb
listed_para=[] #we initialize inputs and output to use in Tb
reserved_words=['\0']#used to check word intialize befor
#check for module name
module_name=input("enter module name: \n")
while name_check(module_name,reserved_words) == 0:
    module_name = input("Enter a valid name:\n")
#end of check  
reserved_words.append(module_name)
f=open(f"C:/Users/marrw/Desktop/{module_name}.v","w")
tb=open(f"C:/Users/marrw/Desktop/{module_name}_TB.v","w")
f.write("module %s \n"%(module_name))
tb.write("module %s_TB();\n"%(module_name))

in_out=[] #we initialize inputs and output to use in Tb
listed_para=[] #we initialize parameter to use in Tb

while True:
    try:
        seq_combi=int(input("do you want 0-seqintial or 1-combintional\n"))
        break  # Exit the loop if the input is a valid floating-point number
    except ValueError:
        print("That's not a valid floating-point number. Please try again.")
        
seq_combi=check_for_booliain(seq_combi)

while True:
    try:
        parameter=int(input("do you want parameter?\n 1-yes :0-no "))
        break  # Exit the loop if the input is a valid floating-point number
    except ValueError:
        print("That's not a valid floating-point number. Please try again.")
#check for right boolean
parameter=check_for_booliain(parameter)

#here we check if the user want right parameter or not 
#here is start of parameter Block
if parameter ==1:
        f.write("#(parameter ")        
        while True:
            try:
                numberPara=int(input("enter number of parameter: \n"))
                break  # Exit the loop if the input is a valid floating-point number
            except ValueError:
                print("That's not a valid floating-point number. Please try again.")
        #handle zero number of parameter condition
        while numberPara ==0:
            while True:
                try:
                    numberPara=int(input("enter a valid number of parameter more than 0: \n"))
                    break  # Exit the loop if the input is a valid floating-point number
                except ValueError:
                    print("That's not a valid floating-point number. Please try again.")
        while 1:            
            #check for parameter name
            para_name=input(f"enter parameter {numberPara} name \n")
            while name_check(para_name,reserved_words) == 0:
                para_name = input("Enter a valid name:\n")
            #end of check   
            # we put name of parameter in list to use it in TB
            listed_para.append(para_name)
            reserved_words.append(para_name)
            while True:
                try:
                    para_value=int(input("enter parameter value\n"))
                    break  # Exit the loop if the input is a valid floating-point number
                except ValueError:
                    print("That's not a valid floating-point number. Please try again.")
           
            ''' in this if statement we check if this parameter 
            is last or not to put in line with ); not ,''' 
    
            if numberPara==1:
                f.write("%s = %d)\n"%(para_name,para_value))
                tb.write("parameter %s_TB =%d ;\n"%(para_name,para_value))
                break
            else:
               f.write("%s = %d,"%(para_name,para_value))
               tb.write("parameter %s_TB =%d ; \n"%(para_name,para_value))
            numberPara=numberPara-1
#here is end of parameter Block

#here is start of input block 

#now we asking if parameterized or not and initialize input
f.write("(")
if seq_combi==0:
    #check for parameter name
    clk_name=input("enter the name of clock:\n")
    while name_check(clk_name,['\0']) == 0:
        clk_name = input("Enter a valid name:\n")
    #end of check
    
    #check for reset name
    reset_name=input("enter name of reset:\n")
    while name_check(reset_name,['\0']) == 0:
        reset_name = input("Enter a valid name:\n")
    #end of check
    in_out.append(clk_name)
    reserved_words.append(reset_name)
    
    in_out.append(reset_name)
    reserved_words.append(reset_name)
    
    f.write(f"input {clk_name},{reset_name},\n")
    tb.write(f"reg {clk_name}_TB;\nreg {reset_name}_TB;\n")
    NoOfInput=int(input("enter number of input without clk and reset:\n"))
else:    
    NoOfInput=int(input("enter number of input:\n"))
while NoOfInput>0:
    #check for input name
    name_input=input(f"enter input {NoOfInput} name \n")
    while name_check(name_input,reserved_words) == 0:
        name_input = input("Enter a valid name:\n")
    while True:
        try:
            parameterIP=int(input("do you want this input parameterized ?\n 1-yes :0-no "))
            break  # Exit the loop if the input is a valid floating-point number
        except ValueError:
            print("That's not a valid floating-point number. Please try again.")
    #check for right boolean
    parameterIP=check_for_booliain(parameterIP)
    if parameterIP ==1:
                        
            #check for parameter name
            para_name1 = input(f"enter parameter name from this list {listed_para}:\n")
            while name_check(para_name1,['\0']) == 0:
                para_name1 = input("Enter a valid name:\n")
            #end of check  
            para_name1=para_check(listed_para,para_name1)
            
            f.write("input ")         
            f.write("[%s-1:0]%s,\n"%(para_name,name_input))
            tb.write("reg [%s-1:0] %s_TB;\n"%(para_name,name_input))
    else:   
            bit_or_vector=int(input("enter 0-bit or 1-vector\n"))
            bit_or_vector=check_for_booliain(bit_or_vector)
            if bit_or_vector ==0:
                f.write("input ")
                
                f.write("%s,\n"%(name_input))
                #we write input name in TB
                tb.write("reg %s_TB ;\n"%(name_input))
                #here we put name of list to use in instantaion
            else:
                while True:
                    try:
                        MSP=int(input("enter MSB:\n"))
                        break  # Exit the loop if the input is a valid floating-point number
                    except ValueError:
                        print("That's not a valid floating-point number. Please try again.")
                while True:
                    try:
                        LSB=int(input("enter LSB:\n"))
                        break  # Exit the loop if the input is a valid floating-point number
                    except ValueError:
                        print("That's not a valid floating-point number. Please try again.")
                f.write("input ")

                f.write(f"[{MSP}:{LSB}]{name_input},\n")
                #we write input name in TB
                tb.write(f"reg [{MSP}:{LSB}]{name_input}_TB  ;\n")
                #here we put name of list to use in instantaion  
   
    
    in_out.append(name_input)
    reserved_words.append(name_input)
    NoOfInput=NoOfInput-1
#now we asking if parameterized or not and initialize output 
while True:
    try:
        NoOfOutput=int(input("enter number of output:\n"))
        break  # Exit the loop if the input is a valid floating-point number
    except ValueError:
        print("That's not a valid floating-point number. Please try again.")
while NoOfOutput>0:
    #check for output name
    out_named=input(f"enter output {NoOfOutput} name:\n")
    while name_check(out_named,reserved_words) == 0:
        out_named = input("Enter a valid name:\n")
    #end of check 
    while True:
        try:
            parameterOP   =int(input("do you want this output parameterized ?\n 1-yes :0-no "))
            break  # Exit the loop if the input is a valid floating-point number
        except ValueError:
            print("That's not a valid floating-point number. Please try again.")
    parameterOP=check_for_booliain(parameterOP)
 
    in_out.append(out_named)
    reserved_words.append(out_named)
    #check for boolean reg or wire 
    while True:
        try:
            out_kind=int(input("enter this output kind (1-reg or 0-wire)"))
            break  # Exit the loop if the input is a valid floating-point number
        except ValueError:
            print("That's not a valid floating-point number. Please try again.")
    out_kind=check_for_booliain(out_kind)
    #end check
    #here if output is parametrized
    if parameterOP ==1:
        #check for parametr of output name
        para_out_name=input(f"enter output name from this list {listed_para}:\n")
        while name_check(out_named,['\0']) == 0:
            out_named = input("Enter a valid name:\n")
        #end of check
        para_out_name=para_check(listed_para,para_out_name)
        
        #check for last element to print );
        if NoOfOutput==1:
            f.write("output reg [%s-1: 0] %s);\n"%(para_out_name,out_named))
            tb.write("wire [%s-1:0] %s_TB;\n"%(para_out_name,out_named))
            break
        #end chek
        
        #check for kind of output 
        if out_kind ==1:
            f.write("output reg [%s-1: 0] %s,\n"%(para_out_name,out_named))
        elif out_kind ==0:
            f.write("output wire [%s-1: 0] %s,\n"%(para_out_name,out_named))
        tb.write("wire [%s-1:0] %s_TB;\n"%(para_out_name,out_named))
        #end check
        
    #here if output not parametrized
    elif parameterOP==0:
        
        while True:
            try:
                bit_or_vectorO=int(input("enter 0-bit or 1-vector\n"))
                break  # Exit the loop if the input is a valid floating-point number
            except ValueError:
                print("That's not a valid floating-point number. Please try again.")
        bit_or_vectoO=check_for_booliain(bit_or_vectorO)
        if bit_or_vectorO ==0:
            if NoOfOutput==1:
                f.write("output reg %s\n"%(out_named))
                tb.write("wire %s_TB;\n"%(out_named))
                break
            if out_kind ==1:
                f.write("output reg %s,\n"%(out_named))
            elif out_kind ==0:
                f.write("output wire %s,\n"%(out_named))
            tb.write("wire %s_TB;\n"%(out_named))
        else:
            while True:
                try:
                    MSPO=int(input("enter MSB :\n"))
                    break  # Exit the loop if the input is a valid floating-point number
                except ValueError:
                    print("That's not a valid floating-point number. Please try again.")
            while True:
                 try:
                     LSBO=int(input("enter LSB :\n"))
                     break  # Exit the loop if the input is a valid floating-point number
                 except ValueError:
                     print("That's not a valid floating-point number. Please try again.")        
        
            if NoOfOutput==1:
                f.write(f"output reg [{MSPO}:{LSBO}] {out_named}\n")
                tb.write(f"wire  [{MSPO}:{LSBO}] {out_named}_TB;\n")
                break
            if out_kind ==1:
                f.write(f"output reg [{MSPO}:{LSBO}] {out_named},\n")
                tb.write(f"wire  [{MSPO}:{LSBO}] {out_named}_TB;\n")
            elif out_kind ==0:
                f.write(f"output wire [{MSPO}:{LSBO}] {out_named},\n")
            tb.write(f"wire [{MSPO}:{LSBO}] {out_named}_TB;\n")
        
            
    NoOfOutput=NoOfOutput-1   
f.write(");\n")
f.write("//-----------------------------\n\n\n\n")


while True:
     try:
         reg_wire=int(input("do you want reg or wires internally?\n 1- ok 0-not ok \n"))
         break  # Exit the loop if the input is a valid floating-point number
     except ValueError:
         print("That's not a valid floating-point number. Please try again.")
#check for right boolean
reg_wire=check_for_booliain(reg_wire)
if  reg_wire==1:
    
    while True:
         try:
             no_wire_reg=int(input("enter number of wire or reg\n"))
             break  # Exit the loop if the input is a valid floating-point number
         except ValueError:
             print("That's not a valid floating-point number. Please try again.")
    while no_wire_reg>0:
        print(no_wire_reg)
        name_rw=input("enter wire or reg name\n")
        while name_check(name_rw,reserved_words) == 0:
            name_rw = input("Enter a valid name:\n")
        #end of check
     
        while True:
             try:
                 choose=int(input("do you want this 0-reg or 1-wires ?\n"))
                 break  # Exit the loop if the input is a valid floating-point number
             except ValueError:
                 print("That's not a valid floating-point number. Please try again.")
        #check for right boolean
        choose=check_for_booliain(choose)
        
        while True:
             try:
                 para_w=int(input("do you want parameterized or not? 1-yes 0-no \n"))
                 break  # Exit the loop if the input is a valid floating-point number
             except ValueError:
                 print("That's not a valid floating-point number. Please try again.")
        #check for right boolean
        para_w=check_for_booliain(para_w)
        
        if para_w==1:
            #end of check
            pr_name=input(f"enter parameter name from this list {listed_para}:\n")
            while name_check(pr_name,['\0']) == 0:
                pr_name = input("Enter a valid name:\n")
            #end of check
            pr_name=para_check(listed_para,pr_name)
            if choose==1:
                f.write("wire [%s-1:0]%s ;\n"%(pr_name,name_rw))
            elif choose==0:
                f.write("reg [%s-1:0]%s ;\n"%(pr_name,name_rw))
        elif para_w==0:
            if choose==1:
                f.write("wire %s ;\n"%(name_rw))
            elif choose==0:
                f.write("reg %s ;\n"%(name_rw))
        no_wire_reg=no_wire_reg-1
f.write("//-----------------------------\n\n\n\n")



f.write("//-----------------------------\n\n\n\n")
f.write("//write here combinational logic\n")
f.write("//-----------------------------\n\n\n\n")
#----------------------
#ask for sequintial or combintional 

if seq_combi == 0:
    
    while True:
         try:
             syn=int(input("do you want 0-synchronous\n1-asynchronous\n"))
             break  # Exit the loop if the input is a valid floating-point number
         except ValueError:
             print("That's not a valid floating-point number. Please try again.")
    #check for right boolean
    syn=check_for_booliain(syn)
    if syn==0:
        
        while True:
             try:
                 edge=int(input("do you want clock and reset to be 0-negedge\n1 -posedge\n"))
                 break  # Exit the loop if the input is a valid floating-point number
             except ValueError:
                 print("That's not a valid floating-point number. Please try again.")
                 
        #check for right boolean
        edge=check_for_booliain(edge)
        if edge==1:
            f.write(f"always@(posedge {clk_name})\n\nbegin\nif({reset_name})begin\n\nend\n\nelse\nbegin\n\nend\nend\n")
        else:
            f.write(f"always@(negedge {clk_name})\n\nbegin\nif({reset_name})begin\n\nend\n\nelse\nbegin\n\nend\nend\n")
    else:
        while True:
             try:
                 state=int(input("do you want clock and reset to be \n\n1-posedge-posedge\n\n2-posedge-negedge\n\n3-negedge-posedge\n\n4-negedge-negedge\n"))
                 break  # Exit the loop if the input is a valid floating-point number
             except ValueError:
                 print("That's not a valid floating-point number. Please try again.")
        state=check_for_syn(state)
        if state==1:
            f.write(f"always@(posedge {clk_name},negedge {reset_name})\nbegin\nif({reset_name})begin\n\nend\nelse\nbegin\n\nend\nend\n")
        elif state==2:
            f.write(f"always@(posedge {clk_name},posedge {reset_name})\nbegin\nif({reset_name})begin\n\nend\nelse\nbegin\n\nend\nend\n")
        elif state==3:
            f.write(f"always@(negedge {clk_name},posedge {reset_name})\nbegin\nif({reset_name})begin\n\nend\nelse\nbegin\n\nend\nend\n")
        elif state==4:
            f.write(f"always@(negedge {clk_name},negedge {reset_name})\nbegin\nif({reset_name})begin\n\nend\nelse\nbegin\n\nend\nend\n")      

f.write("endmodule\n")    
f.close()
######################################### test Bensh instantion##########################################

tb.write("%s "%(module_name))
list_size=len(listed_para)
if list_size >0:
    tb.write("#(")
    for i in range(list_size-1):
        tb.write(".%s(%s_TB),"%(listed_para[i],listed_para[i]))
    tb.write(".%s(%s_TB))"%(listed_para[list_size-1],listed_para[list_size-1]))
tb.write(" dut ")


list2_size=len(in_out)

if list2_size >0:
    tb.write("(")
    for i in range(list2_size-1):
        tb.write(".%s(%s_TB),"%(in_out[i],in_out[i]))
    tb.write(".%s(%s_TB));\n\n"%(in_out[list2_size-1],in_out[list2_size-1]))
elif list2_size==0:
    tb.write("();\n")
if(seq_combi==0):
    
    while True:
         try:
             half_period=int(input("enter the half period time\n"))
             break  # Exit the loop if the input is a valid floating-point number
         except ValueError:
             print("That's not a valid floating-point number. Please try again.")
    tb.write("always #%d clk =~ clk ;\n\n"%(half_period))

tb.write("initial begin\n\n\nend\n\nendmodule")




f.close()
tb.close()