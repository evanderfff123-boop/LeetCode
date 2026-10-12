import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class MHA(nn.Module):
    # d_model: 指的就是隐藏层的大小
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        # nn.Linear 只是定义这个的形状，不是真正的计算，计算是 F.Linear()
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.o = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x):  
        b, s, _ = x.shape
        # b: batch_size; s: seq_len; D: d_model; d: D // n_heads
        # chunk(3, dim=-1): 指的是沿着最后一维平均切成3段
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        # [B, S, D] -> [B, H, S, d]
        # view只改变形状，把(b, s, d_model) -> (b, s, n_heads, d_head)
        # transpose(1, 2), 把第一轴和第二轴对掉: ->(b, n_heads, s, d_head)
        q = q.view(b, s, self.n_heads, self.d_head).transpose(1, 2)
        k = k.view(b, s, self.n_heads, self.d_head).transpose(1, 2)
        v = v.view(b, s, self.n_heads, self.d_head).transpose(1, 2)
        score = q @ k.transpose(-1, -2) / math.sqrt(self.d_head)
        # tril(): triangle lower: 只保留下三角，含对角线，实现mask
        causal = torch.ones(s, s, device=x.device, dtype=torch.bool).tril()
        score = score.masked_fill(~causal, float("-inf"))
        out = torch.softmax(score, dim=-1) @ v     # [B, H, S, d]
        out = out.transpose(1, 2).reshape(b, s, -1)
        return self.o(out)
