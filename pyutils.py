# coding: utf8
import random

class GenList:
    names = ['jack','tom','larry','euler','marry','john','alice','black','white','mike']
    names_zh=['孙悟空','卓一航','张三丰','诸葛亮','武松','赵云','宋高宗','王维','乔峰','虚竹']
    fruits= ['apple','banana','pear','orange','pineapple','mango','strawberry','watermelon','grape','melon']
    fruits_zh=['苹果','橘子','香蕉','梨','草莓','芒果','西瓜','柚子','葡萄','哈密瓜']
    headers={
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 ',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 ',
            'AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'
        )
    }


class Backup:
    @staticmethod
    def backup(src_file, *des_directory): #src_file为要复制的文件,*des_files为要复制到的目录位置
        file_name=src_file[src_file.rindex('\\')+1:] #获取文件名
        for file in des_directory:
            file=file+'\\'+file_name #保存文件的路径
            with open(file,'w',encoding='utf8') as f:
                content = open(src_file,encoding='utf8').read()
                f.write(content,)
        print("恭喜,备份完毕!")


class UsefulApp:
    #n_len名字的长度,n_num生成名字的个数
    @staticmethod
    def genNames(n_len,n_num):
        letters = []
        for xi in range(ord('a'), ord('z') + 1):
            letters.append(chr(xi))
        names = []
        for i in range(n_num):
            name_len=random.randint(3,n_len)
            name = ''.join(random.sample(letters, name_len))
            names.append(name)
        return names

    @staticmethod
    def genN_A(n_len,n_num):
        letters = []
        for xi in range(ord('a'), ord('z') + 1):
            letters.append(chr(xi))
        nas=[]
        for i in range(n_num):
            na = {}
            name_len = random.randint(3, n_len)
            name = ''.join(random.sample(letters, name_len))
            na['name']=name
            na['age']=random.randint(10,100)
            nas.append(na)
        return nas

    @staticmethod
    def genN_A_G_P(n_len, n_num):
        letters = []
        for xi in range(ord('a'), ord('z') + 1):
            letters.append(chr(xi))
        nas = []
        for i in range(n_num):
            na = {}
            name_len = random.randint(3, n_len)
            name = ''.join(random.sample(letters, name_len))
            na['name'] = name
            na['age'] = random.randint(10, 100)
            na['sex'] = random.sample(['男','女'],1)[0]
            na['phone']='1'+str(random.randint(3,9))+str(random.sample(range(100000000,1000000000),1)[0])
            nas.append(na)
        return nas

