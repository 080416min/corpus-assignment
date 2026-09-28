# analysis.py
import jieba
import pandas as pd

# ========== 设置 ==========
target_word = "李氏"
txt_path = "data/jiuzhi.txt"
min_word_length = 2
# ==========================

# 读取文本
with open(txt_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# 分词
words_all = jieba.lcut(raw_text)

# 加载停用词
stopwords = set()
try:
    from qhchina import load_stopwords
    stopwords = set(load_stopwords())
except:
    pass

def get_collocates(word_list, target, window_size):
    collocate_dict = {}
    target_count = word_list.count(target)
    for idx, w in enumerate(word_list):
        if w == target:
            left = max(0, idx-window_size)
            right = min(len(word_list), idx+window_size+1)
            for i in range(left, right):
                if i == idx:
                    continue
                cw = word_list[i]
                if len(cw)>=min_word_length and cw not in stopwords and cw != target:
                    collocate_dict[cw] = collocate_dict.get(cw,0)+1
    rows = []
    for cw, cnt in collocate_dict.items():
        rows.append({"搭配词":cw,"共现次数":cnt,"目标词频次":target_count})
    df = pd.DataFrame(rows)
    return df

exp_list = [
    {"name":"window5", "window":5},
    {"name":"window10","window":10},
    {"name":"sentence","window":999}
]
output_dfs = {}

for exp in exp_list:
    print(f"正在运行：{exp['name']}")
    df = get_collocates(words_all, target_word, exp["window"])
    csv_name = f"output/collocates_{exp['name']}.csv"
    df.to_csv(csv_name, index=False, encoding="utf-8-sig")
    output_dfs[exp["name"]] = df
    print(f"{exp['name']} 保存成功：{csv_name}")

# 生成html
html_parts = []
for name,df in output_dfs.items():
    html_parts.append(f"<h2>实验：{name}</h2>")
    html_parts.append(df.to_html(index=False))

full_html = "<html><body>" + "\n".join(html_parts) + "</body></html>"
with open("output/results.html","w",encoding="utf-8") as f:
    f.write(full_html)

print("✅全部完成！文件输出到output文件夹")
