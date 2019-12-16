#coding:gbk
"""
程序: 完成RPSLS游戏
作者:王蔚
"""

import random
answer=random.randint(0,4)#计算机输出的随机数

# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
       player_choice_number=0
       return player_choice_number
    elif name=="史波克":
       player_choice_number=1
       return player_choice_number
    elif name=="布":
       player_choice_number=2
       return player_choice_number
    elif name=="蜥蜴":
       player_choice_number=3
       return player_choice_number
    elif name=="剪刀":
       player_choice_number=4
       return player_choice_number
    else:
       print("Error: No Correct Name")
		
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        comp_number="石头"
        return comp_number
    elif number==1:
        comp_number="史波克"
        return comp_number
    elif number==2:
        comp_number="布"
        return comp_number
    elif number==3:
        comp_number="蜥蜴"
        return comp_number
    elif number==4:
        comp_number="剪刀"
        return comp_number
		
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    player_choice_number=name_to_number(player_choice)
    comp_number=number_to_name(answer)
    if player_choice_number==answer:
        print("您的选择为:%s"%player_choice)
        print("计算机的选择为:%s"%comp_number)
        print("你和计算机一样呢")
    elif player_choice_number==0 :
        if answer==3 or answer==4:
            print("您的选择为:%s"%player_choice)
            print("计算机的选择为:%s"%comp_number)
            print("您赢了")
        if answer==1 or answer==2:
            print("您的选择为:%s"%player_choice)
            print("计算机的选择为:%s"%comp_number)
            print("计算机赢了")
    elif player_choice_number==1 :
        if answer==0 or answer==4:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("您赢了")
        if answer==2 or answer==3:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("计算机赢了")
    elif player_choice_number==2 :
       if answer==0 or answer==1:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("您赢了")
       if answer==3 or answer==4:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("计算机赢了")
    elif player_choice_number==3 :
       if answer==1 or answer==2:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("您赢了")
       if answer==0 or answer==4:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("计算机赢了")
    elif player_choice_number==4 :
       if answer==3 or answer==2:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("您赢了")
       if answer==1 or answer==0:
           print("您的选择为:%s"%player_choice)
           print("计算机的选择为:%s"%comp_number)
           print("计算机赢了")
		    
print("欢迎使用RPSLS游戏")
print("--------")
print("请输入你的选择:")
player_choice=input()
print("--------")
rpsls(player_choice)

		
    
    
