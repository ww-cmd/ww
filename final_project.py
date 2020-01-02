#coding:gbk
"""
程序:对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化，生成人物关系图谱。
作者:王蔚
"""
import codecs
import jieba.posseg as pseg
import jieba
names={}#保存人物，键为人物名称，值为该人物在全文的出现次数
relationships={}#保存人物之间的关系，代表两个人物之间的紧密程度
lineNames=[]#保存对每一段分词得到当前段中出现的人物名称
jieba.load_userdict("role.txt")#自定义人名，提高识别的准确度
with codecs.open("黎明破晓的街道.txt","r","utf-8") as f:
	for line in f.readlines():
		poss=pseg.cut(line)
		lineNames.append([])
		for w in poss:
			if w.flag!="nr" or len(w.word)<2:
				continue
			lineNames[-1].append(w.word)#增加人物
			if names.get(w.word) is None:
				names[w.word]=0
				relationships[w.word]={}
			names[w.word]+=1
# for name,times in names.items():
	# print(name,times)

for line in lineNames:
	for nameone in line:#将人物之间连接，突出之间的紧密程度
		for nametwo in line:
			if nameone==nametwo:
				continue
			if relationships[nameone].get(nametwo) is None:
				relationships[nameone][nametwo]=1
			else:
				relationships[nameone][nametwo]=relationships[nameone][nametwo]+1
with codecs.open("roles.txt","w","utf-8") as f:#将角色出现次数写入记事本
	f.write("ID Label Weight\r\n" )
	for name,times in names.items():
		if times>10 and name!="小姐" and name!="老公" and name!="阿姨" and name!="平安夜" and name!="滑雪" and name!="明白":
			f.write(name+" "+name+" "+str(times)+"\r\n")	

with codecs.open("roless.txt","w","utf-8") as f:#将角色关系写入记事本
	f.write("Source Target Weight\r\n")
	for name,edges in relationships.items():
		for v,w in edges.items():
			if w>10 and name!="小姐" and name!="老公" and name!="阿姨" and name!="平安夜" and name!="滑雪" and name!="明白":
				f.write(name+" "+v+" "+str(w)+"\r\n")

					
