from collections import defaultdict
import opencc
import json
import os
from tqdm import tqdm

cc = opencc.OpenCC('t2s')

base='quan_tang_shi/json'

new_json=[]
settled=defaultdict(bool)
for file in tqdm(os.listdir(base)):
    

    if 'db' in file or 'md' in file or 'error' in file:
            continue
    
    
    with open(base+'/'+file,encoding='utf8') as f:
        all_data=json.load(f)
        for data in all_data:    
            new_dict={}
            for k,v in data.items():
                

                if k=='volume' or k =='tags' or k=='notes' or k=='no#' or k=='biography' or k=='desc' or k=='name':
                    pass
                elif k=='title':
                    new_dict['title']=cc.convert(v)
                elif k=='paragraphs':
                    new_dict['content']=[cc.convert(text) for text in v]  
                else:
                    new_dict[k]=cc.convert(v)
            
            if len(new_dict)==0:
                continue
            new_json.append(new_dict)

    # new_json=list(set(new_json))        

# new_json = [dict(t) for t in set([tuple(d.items()) for d in new_json])]


content=json.dumps(new_json,ensure_ascii=False,indent=2)
with open('唐诗/data5.json','w',encoding='utf8') as f:
    # json.dump(content,f,ensure_ascii=False)
    f.write(content)

s = cc.convert('採菊東籬下，悠然見南山')
print(s)
