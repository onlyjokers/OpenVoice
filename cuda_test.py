# 用来测试在该环境下 cuda 是否可以使用

import torch
print(torch.cuda.is_available())
