import sys
import random

version = "1.1"

NumberList = None

RangeChoiceMin = input("请输入生成范围的最小值：")
RangeChoiceMax = input("请输入生成范围的最大值：")
NumberChoice = input("请输入生成数量：")
RepeatChoice = input("请选择生成方式（1=重复, 2=不重复）：")

RangeChoiceMax1 = int(RangeChoiceMax) + int(1)

if RepeatChoice == "1":
    NumberList = [random.randint(int(RangeChoiceMin),int(RangeChoiceMax1)) for _ in range(int(NumberChoice))]
elif RepeatChoice == "2":
    NumberList = random.sample(range(int(RangeChoiceMin),int(RangeChoiceMax1)),int(NumberChoice))
else:
    input("参数错误，请重启程序并输入正确的参数")
    sys.exit("参数错误")

print(NumberList)
input("按回车键结束")