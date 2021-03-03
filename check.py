# encoding:utf-8
__author__ = 'gaoqiao'



def base_metabolism(weight,height,age):
    BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    height_1 = height * 0.01
    BMI = weight/(height_1*height_1)
    #print BMI

    body_fat = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * 1
    print "您的基础代谢是: %f 大卡" %BMR
    print "您的体脂率是: %f" %body_fat
    return BMR

def sports_coefficient(BMR,sports):
    if sports == 1:
        TDEE = BMR * 1.2
    elif sports == 2:
        TDEE = BMR * 1.375
    elif sports == 3:
        TDEE = BMR * 1.55
    elif sports == 4:
        TDEE = BMR * 1.725
    elif sports == 5:
        TDEE = BMR * 1.9
    else:
        print "再大就不支持啦!"

    print "您的每日能量消耗是：%f 大卡" %TDEE

if __name__ == '__main__':
    BMR = base_metabolism(65,181,33)
    TDEE = sports_coefficient(BMR,2)

