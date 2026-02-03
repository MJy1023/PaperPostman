# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-02-02 16:23:49 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

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

### 🌟 Identifying and Mitigating Position Bias of Multi-image Vision-Language Models

**Authors:** Xinyu Tian, Shu Zou, Zhaoyuan Yang et al.

**Conference:** CVPR.2025

**[Read Paper](/venue/Tian_Identifying_and_Mitigating_Position_Bias_of_Multi-image_Vision-Language_Models@CVPR2025@CVF)**

The evolution of Large Vision-Language Models (LVLMs) has progressed from single-image understanding to multi-image reasoning. Despite this advancement, our findings indicate that LVLMs struggle to robustly utilize information across multiple images, with predictions significantly affected by the alteration of image positions. To further explore this issue, we introduce Position-wise Question Answering (PQA), a meticulously designed task to quantify reasoning capabilities at each position. Our analysis reveals a pronounced position bias in LVLMs: open-source models excel in reasoning with images positioned later but underperform with those in the middle or at the beginning, while proprietary models like GPT-4o show improved comprehension for images at the beginning and end but struggle with those in the middle. Motivated by these insights, we propose SoFt Attention (SoFA), a simple, training-free approach that mitigates this bias by employing linear interpolation between inter-image causal attention and bidirectional counterparts. Experimental results demonstrate that SoFA effectively reduces position bias and significantly enhances the reasoning performance of existing LVLMs.

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
