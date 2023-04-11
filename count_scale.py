import os
import json
# base='./'
# cnt=0
# for file in os.listdir(base):
#     if 'images' in file or 'mengxue' in file or '.' in file:
#         continue
#     if not os.path.isdir(base+file):
#         continue
    
#     for json_file in os.listdir(base+file):
#         with open(base+file+'/'+json_file,encoding='utf8') as f:
#             content_list=json.load(f)
#         cnt+=len(content_list)

# print(f'数据集总规模：{cnt}个（诗/词/文）')

# cnt_shi=0
# base='唐诗/'
# for json_file in os.listdir(base):
#     with open(base+json_file,encoding='utf8') as f:
#         content_list=json.load(f)
#     cnt_shi+=len(content_list)
# print(f'唐诗：{cnt_shi}个')

# cnt_shi=0
# base='宋词'
# for json_file in os.listdir(base):
#     with open(base+json_file,encoding='utf8') as f:
#         content_list=json.load(f)
#     cnt_shi+=len(content_list)
# print(f'宋词：{cnt_shi}个')

cnt_shi=0
base='千家诗/'
for json_file in os.listdir(base):
    with open(base+json_file,encoding='utf8') as f:
        content_list=json.load(f)
    cnt_shi+=len(content_list)
print(f'千家诗：{cnt_shi}个')