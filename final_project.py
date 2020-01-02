#coding:gbk
"""
����:�ԡ����������Ľֵ����ı��������ϵ����ȡ��������Gelphi����������ϵ���ӻ������������ϵͼ�ס�
����:��ε
"""
import codecs
import jieba.posseg as pseg
import jieba
names={}#���������Ϊ�������ƣ�ֵΪ��������ȫ�ĵĳ��ִ���
relationships={}#��������֮��Ĺ�ϵ��������������֮��Ľ��̶ܳ�
lineNames=[]#�����ÿһ�ηִʵõ���ǰ���г��ֵ���������
jieba.load_userdict("role.txt")#�Զ������������ʶ���׼ȷ��
with codecs.open("���������Ľֵ�.txt","r","utf-8") as f:
	for line in f.readlines():
		poss=pseg.cut(line)
		lineNames.append([])
		for w in poss:
			if w.flag!="nr" or len(w.word)<2:
				continue
			lineNames[-1].append(w.word)#��������
			if names.get(w.word) is None:
				names[w.word]=0
				relationships[w.word]={}
			names[w.word]+=1
# for name,times in names.items():
	# print(name,times)

for line in lineNames:
	for nameone in line:#������֮�����ӣ�ͻ��֮��Ľ��̶ܳ�
		for nametwo in line:
			if nameone==nametwo:
				continue
			if relationships[nameone].get(nametwo) is None:
				relationships[nameone][nametwo]=1
			else:
				relationships[nameone][nametwo]=relationships[nameone][nametwo]+1
with codecs.open("roles.txt","w","utf-8") as f:#����ɫ���ִ���д����±�
	f.write("ID Label Weight\r\n" )
	for name,times in names.items():
		if times>10 and name!="С��" and name!="�Ϲ�" and name!="����" and name!="ƽ��ҹ" and name!="��ѩ" and name!="����":
			f.write(name+" "+name+" "+str(times)+"\r\n")	

with codecs.open("roless.txt","w","utf-8") as f:#����ɫ��ϵд����±�
	f.write("Source Target Weight\r\n")
	for name,edges in relationships.items():
		for v,w in edges.items():
			if w>10 and name!="С��" and name!="�Ϲ�" and name!="����" and name!="ƽ��ҹ" and name!="��ѩ" and name!="����":
				f.write(name+" "+v+" "+str(w)+"\r\n")

					
