#coding:gbk
"""
����: ���RPSLS��Ϸ
����:��ε
"""

import random
answer=random.randint(0,4)#���������������

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
       player_choice_number=0
       return player_choice_number
    elif name=="ʷ����":
       player_choice_number=1
       return player_choice_number
    elif name=="��":
       player_choice_number=2
       return player_choice_number
    elif name=="����":
       player_choice_number=3
       return player_choice_number
    elif name=="����":
       player_choice_number=4
       return player_choice_number
    else:
       print("Error: No Correct Name")
		
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        comp_number="ʯͷ"
        return comp_number
    elif number==1:
        comp_number="ʷ����"
        return comp_number
    elif number==2:
        comp_number="��"
        return comp_number
    elif number==3:
        comp_number="����"
        return comp_number
    elif number==4:
        comp_number="����"
        return comp_number
		
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    player_choice_number=name_to_number(player_choice)
    comp_number=number_to_name(answer)
    if player_choice_number==answer:
        print("����ѡ��Ϊ:%s"%player_choice)
        print("�������ѡ��Ϊ:%s"%comp_number)
        print("��ͼ����һ����")
    elif player_choice_number==0 :
        if answer==3 or answer==4:
            print("����ѡ��Ϊ:%s"%player_choice)
            print("�������ѡ��Ϊ:%s"%comp_number)
            print("��Ӯ��")
        if answer==1 or answer==2:
            print("����ѡ��Ϊ:%s"%player_choice)
            print("�������ѡ��Ϊ:%s"%comp_number)
            print("�����Ӯ��")
    elif player_choice_number==1 :
        if answer==0 or answer==4:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("��Ӯ��")
        if answer==2 or answer==3:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("�����Ӯ��")
    elif player_choice_number==2 :
       if answer==0 or answer==1:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("��Ӯ��")
       if answer==3 or answer==4:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("�����Ӯ��")
    elif player_choice_number==3 :
       if answer==1 or answer==2:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("��Ӯ��")
       if answer==0 or answer==4:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("�����Ӯ��")
    elif player_choice_number==4 :
       if answer==3 or answer==2:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("��Ӯ��")
       if answer==1 or answer==0:
           print("����ѡ��Ϊ:%s"%player_choice)
           print("�������ѡ��Ϊ:%s"%comp_number)
           print("�����Ӯ��")
		    
print("��ӭʹ��RPSLS��Ϸ")
print("--------")
print("���������ѡ��:")
player_choice=input()
print("--------")
rpsls(player_choice)

		
    
    
