# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-07-17 16:56:40 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

**Authors:** Chufan Shi, Cheng Yang, Yaokang Wu et al.

**Conference:** ICML.2026

**[Read Paper](/venue/DdU1o2ZvWi@OpenReview)**

Vision-Language Models (VLMs) often produce self-reflective statements like “let me check the figure again” during reasoning. Do such state- ments trigger genuine visual re-examination, or are they merely learned textual patterns? We in- vestigate this via VISUALSWAP, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-BENCH, 800 image pairs curated from MathVista, Math- Verse, MathVision, and MMMU-Pro. Exper- iments on Qwen3-VL, Kimi-VL, and ERNIE- VL reveal a striking failure: models overwhelm- ingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking mod- els are nearly 3x more vulnerable than their in- structed counterparts, and scaling offers no mit- igation. Multi-turn user instructions restore vi- sual grounding, but self-generated reflective state- ments during continuous generation do not. At- tention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io/

### 🌟 ViG-RAG: Video-aware Graph Retrieval-Augmented Generation via Temporal and Semantic Hybrid Reasoning

**Authors:** Zongsheng Cao, Anran Liu, Yangfan He et al.

**Conference:** AAAI.2026

**[Read Paper](/venue/36963@AAAI)**

Retrieval-augmented generation (RAG) has greatly improved Large Language Models (LLMs) by adding external knowledge. However, current RAG-based methods face difficulties with long-context video understanding due to two main challenges. First, Current RAG-based methods for long-context video understanding struggle to effectively integrate multimodal and long-range temporal information, resulting in fragmented and context-insensitive knowledge representations. Furthermore, their retrieval mechanisms often rely on static textual matching, failing to dynamically align user queries with the most relevant video segments and leading to suboptimal downstream performance. To overcome these issues, we introduce ViG-RAG, a new framework to enhance long-context video understanding through structured textual knowledge grounding and multi-modal retrieval. Specifically, we segment video transcripts into structured units, extract key entities, form temporal connections, and assign confidence for evidence, enabling coherent long-range reasoning. In this way, it utilizes a knowledge-aware grounding mechanism and a context-aware retrieval process that dynamically builds a probabilistic temporal knowledge graph to organize multi-video content. To improve retrieval accuracy, we propose a hybrid retrieval strategy for semantic and temporal features, with an adaptive distribution modeling the relevance. In this way, it achieves the optimal retrieval distribution for each query, enhancing generation efficiency by reducing unnecessary computations. On top of this, ViG-RAG uses a vision-language model to integrate semantic anchors, expanded contextual fields, and selected video frames, generating an accurate response. We evaluate ViG-RAG on several benchmarks, demonstrating that it significantly surpasses current RAG-based methods.

### 🌟 PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

**Authors:** Ruiqi Wang, Dezhong Zhao, Ziqin Yuan et al.

**Conference:** NeurIPS.2025

**[Read Paper](/venue/4xvE6Iy77Y@OpenReview)**

Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for teaching robots complex behaviors without reward engineering. However, its effectiveness is often limited by two critical challenges: the reliance on extensive human input and the inherent difficulties in resolving query ambiguity and credit assignment during reward learning. In this paper, we introduce PRIMT, a PbRL framework designed to overcome these challenges by leveraging foundation models (FMs) for multimodal synthetic feedback and trajectory synthesis. Unlike prior approaches that rely on single-modality FM evaluations, PRIMT employs a hierarchical neuro-symbolic fusion strategy, integrating the complementary strengths of vision-language models (VLMs) and large language models (LLMs) in evaluating robot behaviors for more reliable and comprehensive feedback. PRIMT also incorporates foresight trajectory generation to warm-start the trajectory buffer with bootstrapped samples, reducing early-stage query ambiguity, and hindsight trajectory augmentation for counterfactual reasoning with a causal auxiliary loss to improve credit assignment. We evaluate PRIMT on 2 locomotion and 6 manipulation tasks on various benchmarks, demonstrating superior performance over FM-based and scripted baselines. Website at https://primt25.github.io/.

---


## Weekly Summary

*Week ending 2026-07-17*

---

*No papers to summarize this week.*

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
