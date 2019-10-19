import PySimpleGUI27 as sg
import os
def dir_list(head_dir,dir_name):
	path=[]
	for root,dirs,files in os.walk(head_dir):
		for d in dirs:
			if d==dir_name:
				path.append(os.path.join(root,d))
		for f in files:
			if f ==dir_name:
				path.append(os.path.join(root,f))
	return path
sg.ChangeLookAndFeel('Dark')      
sg.SetOptions(element_padding=(0,0))      
layout = [[sg.Text('File manager',text_color='powderblue',pad=((3,10),10))],
            [sg.Text('Choose Folder to mkdir or mkfile or search:',pad=((3,10),10)),sg.Input(), sg.FolderBrowse()],
            [sg.Text('Remove Folder                    :',pad=((3,10),10)),sg.Input(), sg.FolderBrowse()],
            [sg.Text('Choose file to delete            :',pad=((3,10),10)),sg.Input(),sg.FileBrowse()],
            [sg.Text('Choose file to copy              :',pad=((3,10),10)),sg.Input(),sg.FileBrowse()],
            [sg.Text('The Path to Paste File          :',pad=((3,10),10)),sg.Input(), sg.FolderBrowse()],
            [sg.Text('1- mkdir name                       :',pad=((3,10),10)),sg.Input()],
            [sg.Text('2- mkfile name                      :',pad=((3,10),10)),sg.Input()],
            [sg.Text("3- Search file                      :",pad=((3,10),20)),sg.Input()],
            [sg.Submit(), sg.Exit()],
            [sg.Text("By Miss.Robot",pad=((3,10),20))]
             ]

window = sg.Window('File Manager', layout)
while True:
	event, values=window.Read()
	if event=='Exit':
		break
	elif values[0] != '' and values[5] !='':
		folder=values[0]
		name=values[5]
		os.system(('mkdir '+(folder+"/"+name)))
		print(folder+","+name)
	elif values[0] !='' and values[6] !='':
		folder=values[0]
		name=values[6]
		os.system("touch "+(folder+"/"+name))
		print("hello")
	elif values[1] !='':
		folder=values[1]
		os.system("rm -r "+(folder))
		print("hello")
	elif values[2] !='':
		folder=values[1]
		name=values[2]
		os.system("rm "+name)
		print("hello")
	elif values[3] !='' and values[4] !='':
		folder=values[3]
		path=values[4]
		os.system("cp "+folder+" "+path+"/")
	elif values[7]!='' and values[0]!='':
		path=values[0]
		namefile=values[7]
		listfile=dir_list(path,namefile)
		sg.Popup("The File Found in :",[i for i in listfile])
																						#By Miss.Robot
