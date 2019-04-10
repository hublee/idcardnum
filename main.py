from tkinter import *
# import tkMessageBox
from tkinter.messagebox import *
from idcard import *

root=Tk()

def initSelect():
	pass

	# root.title("New England")
	
	# label = Label(root,text="请选择省份")
	# label.pack()
	
	# yscroll = Scrollbar(root, orient=VERTICAL)
	# # yscroll.grid(row=0,column=2,rowspan=4,padx=(0,100),pady=5,sticky=NS)
	# statesList = ['广东','广西','江西','湖南','广东','广西','江西','湖南','广东','广西']
	# conOFlstNE = StringVar()
	# lstNE = Listbox(root,width=14,height=4,listvariable=conOFlstNE,yscrollcommand=yscroll.set)
	# # lstNE.grid(row=0,column=1,rowspan=4,padx=(100,0),pady=5,sticky=E)
	# conOFlstNE.set(tuple(statesList))
	# yscroll["command"] = lstNE.yview
	# lstNE.pack()

	# Label(lstNE,text='请选择省份').pack()

	#单选
	# LB1=Listbox(root, selectmode = MULTIPLE)
	 
	# #创建Scrollbar
	# yscrollbar = Scrollbar(LB1)
	# yscrollbar.pack(side=RIGHT, fill=Y)
	# yscrollbar.config(command=LB1.yview)

	# Label(root,text='请选择省份').pack()
	# for item in ['广东','广西','江西','湖南','广东','广西','江西','湖南','广东','广西','江西','湖南','广东','广西','江西','湖南','广东','广西','江西','湖南']:
	#     LB1.insert(END,item)
	

	# LB1.pack()


	# LB2=Listbox(root)
	 
	# Label(root,text='请选择城市').pack()
	# for item in ['广州','深圳','南昌','长沙']:
	#     LB2.insert(END,item)
	# LB2.pack()

def initInput():
	Label(root, text="").grid(row=0)
	Label(root, text="    身份证号：").grid(row=1, column=0)
	Entry(root, bd =2,width=40, textvariable = idnumInput).grid(row=1, column=1, columnspan=1)


	Label(root, text="    生成结果：").grid(row=2, column=0)
	# Label(root, text="    注册时间>=：").grid(row=3, column=0)
	# Label(root, text="    性别：", width=5).grid(row=4, column=0)
	# Label(root, text=" 年龄范围：", width=8).grid(row=5, column=0)
	# Label(root, text=" 登录时间：").grid(row=6, column=0)

	
	global idListInput
	idListInput = Text(root, bd =2,height=30)
	idListInput.grid(row=2, column=1, columnspan=2)

	# Entry(root, bd =2, textvariable = cityInput).grid(row=2, column=1, columnspan=1)

	# valid_cmd = root.register(validNum)

	# Entry(root, bd =2, textvariable=logiNtimeInput, validate='key', validatecommand=(valid_cmd, '%P')).grid(row=3, column=1)
	# Label(root, text="(格式:20190102)").grid(row=3, column=2)

	# Radiobutton(root, text='男', variable=sexVal, value=1, width=2).grid(row=4, column=1, sticky=W)
	# Radiobutton(root, text='女', variable=sexVal, value=2, width=2).grid(row=4, column=2, sticky=W)

	# Entry(root, bd =2, textvariable=ageFromVal, validate='key',width=5, validatecommand=(valid_cmd, '%P')).grid(row=5, column=1, sticky=W)
	# Entry(root, bd =2, textvariable=ageToVal, validate='key', width=5, validatecommand=(valid_cmd, '%P')).grid(row=5, column=2, sticky=W)
	# Checkbutton(root, text='今天', variable=loginVal, onvalue=1, width=2).grid(row=6, column=1, sticky=W)
	# Checkbutton(root, text='一周内', variable=loginVal, onvalue=2, width=4).grid(row=6, column=2, sticky=W)
	# Checkbutton(root, text='一月内', variable=loginVal, onvalue=3, width=4).grid(row=6, column=3, sticky=W)

	# Label(root, text="").grid(row=6)
	Button(root, text="生成", command = genIdnums).grid(row=1, column=2, columnspan=1)

def genIdnums():
	idnum = idnumInput.get()
	if not idnum:
		showinfo('错误提示','原始身份证不能为空')
		return
	idlist = a(idnum)
	# showinfo('错误提示', str(idlist))
	# idListInput.set(str(idlist))
	
	global idListInput
	# idListInput.set('')
	# idListInput.clear()
	for i in range(len(idlist)):
		idListInput.insert("end", '\n'+idlist[i])


idnumInput = StringVar()
idListInput = None

if __name__ == '__main__':
	frame_root = Frame(root) 
	initInput()
	root.title('身份证生成器')
	root.geometry("600x300")
	root.resizable(0, 0)
	root.mainloop()

	
