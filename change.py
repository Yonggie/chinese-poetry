import opencc
import json
import os

cc = opencc.OpenCC('t2s')

with open('sishuwujing/mengzi.json',encoding='utf8') as f:
    all_data=json.load(f)
    new_json=[]
    
    for data in all_data:
        new_dict={}
        for k,v in data.items():
            if k=='paragraphs':
                new_dict['content']=[cc.convert(text) for text in v]  
            else:
                new_dict[k]=cc.convert(v)
            
        new_json.append(new_dict)

content=json.dumps(new_json,ensure_ascii=False,indent=2)
with open('四书五经/data.json','w',encoding='utf8') as f:
    # json.dump(content,f,ensure_ascii=False)
    f.write(content)

s = cc.convert('採菊東籬下，悠然見南山')
print(s)
