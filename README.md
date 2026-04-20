# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-04-20 16:54:51 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 ViG-RAG: Video-aware Graph Retrieval-Augmented Generation via Temporal and Semantic Hybrid Reasoning

**Authors:** Zongsheng Cao, Anran Liu, Yangfan He et al.

**Conference:** AAAI.2026

**[Read Paper](/venue/36963@AAAI)**

Retrieval-augmented generation (RAG) has greatly improved Large Language Models (LLMs) by adding external knowledge. However, current RAG-based methods face difficulties with long-context video understanding due to two main challenges. First, Current RAG-based methods for long-context video understanding struggle to effectively integrate multimodal and long-range temporal information, resulting in fragmented and context-insensitive knowledge representations. Furthermore, their retrieval mechanisms often rely on static textual matching, failing to dynamically align user queries with the most relevant video segments and leading to suboptimal downstream performance. To overcome these issues, we introduce ViG-RAG, a new framework to enhance long-context video understanding through structured textual knowledge grounding and multi-modal retrieval. Specifically, we segment video transcripts into structured units, extract key entities, form temporal connections, and assign confidence for evidence, enabling coherent long-range reasoning. In this way, it utilizes a knowledge-aware grounding mechanism and a context-aware retrieval process that dynamically builds a probabilistic temporal knowledge graph to organize multi-video content. To improve retrieval accuracy, we propose a hybrid retrieval strategy for semantic and temporal features, with an adaptive distribution modeling the relevance. In this way, it achieves the optimal retrieval distribution for each query, enhancing generation efficiency by reducing unnecessary computations. On top of this, ViG-RAG uses a vision-language model to integrate semantic anchors, expanded contextual fields, and selected video frames, generating an accurate response. We evaluate ViG-RAG on several benchmarks, demonstrating that it significantly surpasses current RAG-based methods.

### 🌟 Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models

**Authors:** Matt Deitke, Christopher Clark, Sangho Lee et al.

**Conference:** CVPR.2025

**[Read Paper](/venue/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art@CVPR2025@CVF)**

Today's most advanced vision-language models (VLMs) remain proprietary. The strongest open-weight models rely heavily on synthetic data from proprietary VLMs to achieve good performance, effectively distilling these closed VLMs into open ones. As a result, the community has been missing foundational knowledge about how to build performant VLMs from scratch. We present \textbf{Molmo}, a new family of VLMs that are state-of-the-art in their class of openness. Our key contribution is a collection of new datasets, including a dataset of highly detailed image captions for pre-training called \textbf{PixMo}, a free-form image Q\&A dataset for fine-tuning, and an innovative 2D pointing dataset, all collected without the use of external VLMs. The success of our approach relies on careful modeling choices, a well-tuned training pipeline, and, most critically, the quality of our newly collected datasets. Our best-in-class 72B model not only outperforms others in the class of open weight and data models, but also outperforms larger proprietary models including Claude 3.5 Sonnet, and Gemini 1.5 Pro and Flash, second only to GPT-4o based on both academic benchmarks and on a large human evaluation. Our model weights, new datasets, and source code will all be released.

### 🌟 PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

**Authors:** Ruiqi Wang, Dezhong Zhao, Ziqin Yuan et al.

**Conference:** NeurIPS.2025

**[Read Paper](/venue/4xvE6Iy77Y@OpenReview)**

Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for teaching robots complex behaviors without reward engineering. However, its effectiveness is often limited by two critical challenges: the reliance on extensive human input and the inherent difficulties in resolving query ambiguity and credit assignment during reward learning. In this paper, we introduce PRIMT, a PbRL framework designed to overcome these challenges by leveraging foundation models (FMs) for multimodal synthetic feedback and trajectory synthesis. Unlike prior approaches that rely on single-modality FM evaluations, PRIMT employs a hierarchical neuro-symbolic fusion strategy, integrating the complementary strengths of vision-language models (VLMs) and large language models (LLMs) in evaluating robot behaviors for more reliable and comprehensive feedback. PRIMT also incorporates foresight trajectory generation to warm-start the trajectory buffer with bootstrapped samples, reducing early-stage query ambiguity, and hindsight trajectory augmentation for counterfactual reasoning with a causal auxiliary loss to improve credit assignment. We evaluate PRIMT on 2 locomotion and 6 manipulation tasks on various benchmarks, demonstrating superior performance over FM-based and scripted baselines. Website at https://primt25.github.io/.

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
