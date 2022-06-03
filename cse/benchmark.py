import torch
import torch.fx as fx
from functorch import make_fx
import random
from torch.profiler import profile, record_function, ProfilerActivity

from functorch._src.cse import fx_graph_cse

# @torch.jit.script
# def f(x):
#     vals = [x]
#     ops = [torch.clone, torch.cos, torch.tanh, torch.nn.functional.gelu]
#     for _ in range(100): 
#         new_val = random.choice(ops)(random.choice(vals))
#         vals.append(new_val)
#     return vals[-1]


# def f(x):
#     a = x.sum()
#     b = x.sum()
#     c = x.sum()
#     d = x.sum()
#     return a + b + c + d

def profile_it(f, inp):
    for _ in range(5):
        f(inp)

    itr = 5
    with profile(activities=[ProfilerActivity.CUDA], record_shapes=True) as prof:
        for _ in range(itr):
            f(inp)

    timing = prof.key_averages()
    # timing_table = timing.table(sort_by="cuda_time_total", row_limit=10)
    # print(timing_table)
    cuda_time_total = 0
    for e in timing:
        cuda_time_total = cuda_time_total + e.cuda_time_total
    return cuda_time_total / itr

    # print(type(timing)) [FunctionEventAvg]
    

def profile_function(name, f, inp):
    fx_g =  make_fx(f)(inp)
   
    new_g = fx_graph_cse(fx_g.graph)
    new_g = fx.GraphModule(fx_g, new_g)
    # do not benchmark against the scripted version because script already does some CSE
    # script_f = torch.jit.script(fx_g)
    # script_g = torch.jit.script(new_g)
    # avg_cuda_time_f = profile_it(script_f, inp)
    # avg_cuda_time_g = profile_it(script_g, inp)
    avg_cuda_time_f = profile_it(fx_g, inp)
    avg_cuda_time_g = profile_it(new_g, inp)
    num_node_decrease = len(fx_g.graph.nodes) - len(new_g.graph.nodes)

    print(f"{name}, {avg_cuda_time_f}, {avg_cuda_time_g}, {num_node_decrease}, {len(fx_g.graph.nodes)}")

g_gpu = torch.Generator(device='cuda')
g_gpu.manual_seed(2147483647)
inp = torch.randn(2**20, device='cuda', generator=g_gpu) # increase input size

def f1(x):
 return x.cos().cos()

profile_function("f1", f1, inp)

def fsum(x):
    a = x.sum()
    b = x.sum()
    c = x.sum()
    d = x.sum()
    return a + b + c + d

profile_function("fsum", fsum, inp)

def fconcat(x):
    a = torch.cat((x, x))
    b = torch.cat((x, x))
    return a + b
profile_function("fconcat", fconcat, inp)

def fsum2(x):
    a = x.sum()
    for _ in range(30):
        a = a+x.sum()
    return a

profile_function("fsum2", fsum2, inp)

def fsummulti(x):
    a = 0
    for _ in range(3):
        a = a+x.sum()
        a = a*x.sum()
    return a

profile_function("fsummulti", fsummulti, inp)

def fsummulti2(x):
    a = 0
    for _ in range(30):
        a = a+x.sum()
        a = a*x.sum()
    return a

profile_function("fsummulti2", fsummulti2, inp)

def fcos(x):
    a = 0
    for _ in range(3):
        a = a+x.cos()
    return a

profile_function("fcos", fcos, inp)

def fcos2(x):
    a = 0
    for _ in range(30):
        a = a+x.cos()
    return a

profile_function("fcos2", fcos2, inp)





# print(type(fx_g))
# fx_g = fx.symbolic_trace(f)
# fx_g.graph.eliminate_dead_code()
# fx_g.recompile()