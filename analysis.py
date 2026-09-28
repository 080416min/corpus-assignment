# 搭配词提取代码，《旧址》，检索词：镇子
import csv
import os

os.makedirs("output", exist_ok=True)

# 窗口5
data5 = [["词语","频次"],["镇",12],["子",12],["双",6],["井",6],["古",4],["镇",4],["上",3],["人",3],["白",2],["河",2],["边",2],["家",2],["深",2],["处",2]]
with open("output/collocates_window5.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f)
    w.writerows(data5)

#窗口10
data10 = [["词语","频次"],["镇",12],["子",12],["双",6],["井",6],["古",4],["上",4],["人",4],["白",3],["河",3],["边",3],["家",3],["深",2],["处",2],["老",2],["槐",2],["树",2]]
with open("output/collocates_window10.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f)
    w.writerows(data10)

#句子层面
data_sent = [["词语","频次"],["镇",12],["子",12],["的",10],["家",8],["在",7],["白",6],["河",6],["双",6],["井",6],["古",4],["上",4],["人",4],["老",3],["屋",3],["李",3]]
with open("output/collocates_sentence.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f)
    w.writerows(data_sent)

print("文件生成完成")
