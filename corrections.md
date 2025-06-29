**Section:** Our journey up to now

**Context:** Having read both, you should have almost all the core knowledge you need to fully understand how high-performing LLMs are being built nowadays and will just be missing the secret sauce regarding data mixing and architecture choices to complete the recipe (stay tuned for part three…).

**Error:** `how how`


**Section:** Activation recomputation

**Context:** In general, we can do better than full. The authors of the recomputation paper did a detailed analysis studying which activations grow the largest and have the cheapest recomputation cost in terms of floating-point operations per second (FLOPS). It turns out that the attention computations fall in that category, and thus we can usually discard them and focus on checkpointing the expensive feedforward computations.

**Error:** `recomputation`


**Section:** FlashAttention

**Context:** In comparison to FlashAttention-1, the improvements in FlashAttention-2 and -3 are less about the general attention mechanism and more about tailoring its low-level implementation more specifically to the GPU by (1) reducing the number of non-matmul operations as much as possible, (2) carefully partitioning the workload among wraps and thread blocks (for FlashAttention-2), and (3) carefully optimizing for FP8 and Tensor Core support on the latest Hopper (H100) architecture for FlashAttention-3.

**Error:** `wraps`


**Section:** Pipeline Parallelism

**Context:** This choice is explained in detail in the "Breadth-Fist Pipeline Parallelism" paper.

**Error:** `Breadth-Fist`


**Section:** Profiling GPU compute and communication

**Context:** The trace shows: * A CPU threads launching kernels asynchronously on the GPU * Multiple CUDA streams handling compute and communication in parallel * Kernel execution times and memory allocation

**Error:** `A CPU threads`


**Section:** 5D Parallelism in a Nutshell

**Context:** We'll start by comparing pipeline parallelism and ZeRO-3 side-by-side, as they have some very close similarities but also important differences.

**Error:** `are` should be `and`.


**Section:** 5D Parallelism in a Nutshell

**Context:** ...partitioning experts across GPUs becomes relevant when models scale to a large number of experts.

**Error:** `scales` should be `scale`. This is a subject-verb agreement error.


**Section:** Step 1: Fitting a training step in memory

**Context:** At 512+ GPU scale, pure data parallelism/ZeRO-3 will start to become inefficient due to communication cost...

**Error:** `becomes` should be `become`. This is a subject-verb agreement error.


**Section:** Step 1: Fitting a training step in memory

**Context:** We focus on fitting a single instance for now - even though we may use DP for ZeRO to achieve this goal - we're only interested here in the model parameters memory savings that it provides when used with ZeRO-3.

**Error:** `provide` should be `provides`. This is a subject-verb agreement error.


**Section:** Lessons learned on benchmarking

**Context:** ...we hope we can help make distributed training techniques more accessible...

**Error:** `help making` is grammatically incorrect. It should be `help make`.


**Section:** Diving into the GPUs – Fusing, Threading, and Mixing

**Context:** _Registers_ are the smallest units and are private to the threads during execution.

**Error:** `executions` should be the singular `execution`.


**Section:** FlashAttention

**Context:** The global memory in modern GPUs often uses a technology called [High Bandwidth Memory (HBM)](https://semianalysis.com/2024/09/03/the-memory-wall/#hbm-roadmap)...

**Error:** The empty square brackets `[]`


**Section:** A0: Parallel Programming Crash Course

**Context:** def init\_process(): dist.init_process_group(backend='nccl')

**Error:** In the code snippet, `initi_process_group` is a typo and should be `init_process_group`.


**Section:** A0: Parallel Programming Crash Course

**Context:** init\_process() example_broadcast()

**Error:** In the code snippet, `example\_broadcats()` is a typo and should be `example_broadcast()`.


**Section:** A1: Distributed Training Profiling

**Context:** The _.cu_ file would look like this for a simple `add` kernel:

**Error:** `would like this` is grammatically incorrect in this context and should be `would look like this`.


**Section:** A3: Math for Compute/Communication Overlap

**Context:** ...the communication of parameters for the next layer can be hidden behind the computation of the current layer.

**Error:** There is an extraneous backtick `` at the end of the "ZeRO-3 (FSDP) communication analysis" section.


**Section:** A3: Math for Compute/Communication Overlap

**Context:** Interestingly, the ratio only depends on the hidden size h and tensor parallelism degree TP, not on sequence length or batch size.

**Error:** `tp` should be `TP` to be consistent with its usage throughout the rest of the document.