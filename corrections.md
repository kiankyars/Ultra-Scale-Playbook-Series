**Section:** Our journey up to now
**Context:** Having read both, you should have almost all the core knowledge you need to fully understand how how high-performing LLMs are being built nowadays and will just be missing the secret sauce regarding data mixing and architecture choices to complete the recipe (stay tuned for part three…).
**Error:** `how how`

***

**Section:** Activation recomputation
**Context:** In general, we can do better than full. The authors of the recomputation paper did a detailed analysis studying which activations grow the largest and have the cheapest recomputation cost in terms of floating-point operations per second (FLOPS). It turns out that the attention computations fall in that category, and thus we can usually discard them and focus on checkpointing the expensive feedforward computations.
**Error:** `recomputation`

***

**Section:** FlashAttention
**Context:** In comparison to FlashAttention-1, the improvements in FlashAttention-2 and -3 are less about the general attention mechanism and more about tailoring its low-level implementation more specifically to the GPU by (1) reducing the number of non-matmul operations as much as possible, (2) carefully partitioning the workload among wraps and thread blocks (for FlashAttention-2), and (3) carefully optimizing for FP8 and Tensor Core support on the latest Hopper (H100) architecture for FlashAttention-3.
**Error:** `wraps`

***

**Section:** Pipeline Parallelism
**Context:** This choice is explained in detail in the "Breadth-Fist Pipeline Parallelism" paper.
**Error:** `Breadth-Fist`

**Section:** Profiling GPU compute and communication
**Context:** The trace shows: * A CPU threads launching kernels asynchronously on the GPU * Multiple CUDA streams handling compute and communication in parallel * Kernel execution times and memory allocation
**Error:** `A CPU threads`