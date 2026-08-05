# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-08-04 17:27:33 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

**Authors:** Chufan Shi, Cheng Yang, Yaokang Wu et al.

**Conference:** ICML.2026

**[Read Paper](/venue/DdU1o2ZvWi@OpenReview)**

Vision-Language Models (VLMs) often produce self-reflective statements like “let me check the figure again” during reasoning. Do such state- ments trigger genuine visual re-examination, or are they merely learned textual patterns? We in- vestigate this via VISUALSWAP, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-BENCH, 800 image pairs curated from MathVista, Math- Verse, MathVision, and MMMU-Pro. Exper- iments on Qwen3-VL, Kimi-VL, and ERNIE- VL reveal a striking failure: models overwhelm- ingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking mod- els are nearly 3x more vulnerable than their in- structed counterparts, and scaling offers no mit- igation. Multi-turn user instructions restore vi- sual grounding, but self-generated reflective state- ments during continuous generation do not. At- tention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io/

### 🌟 PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

**Authors:** Ruiqi Wang, Dezhong Zhao, Ziqin Yuan et al.

**Conference:** NeurIPS.2025

**[Read Paper](/venue/4xvE6Iy77Y@OpenReview)**

Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for teaching robots complex behaviors without reward engineering. However, its effectiveness is often limited by two critical challenges: the reliance on extensive human input and the inherent difficulties in resolving query ambiguity and credit assignment during reward learning. In this paper, we introduce PRIMT, a PbRL framework designed to overcome these challenges by leveraging foundation models (FMs) for multimodal synthetic feedback and trajectory synthesis. Unlike prior approaches that rely on single-modality FM evaluations, PRIMT employs a hierarchical neuro-symbolic fusion strategy, integrating the complementary strengths of vision-language models (VLMs) and large language models (LLMs) in evaluating robot behaviors for more reliable and comprehensive feedback. PRIMT also incorporates foresight trajectory generation to warm-start the trajectory buffer with bootstrapped samples, reducing early-stage query ambiguity, and hindsight trajectory augmentation for counterfactual reasoning with a causal auxiliary loss to improve credit assignment. We evaluate PRIMT on 2 locomotion and 6 manipulation tasks on various benchmarks, demonstrating superior performance over FM-based and scripted baselines. Website at https://primt25.github.io/.

### 🌟 Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models

**Authors:** Yifu Chen, Shengpeng Ji, Zhengqing Liu et al.

**Conference:** ACL.2026

**[Read Paper](/venue/2026.acl-long.6@ACL)**

Achieving seamless, human-like interaction remains a key challenge for full-duplex spoken dialogue models (SDMs). Reinforcement learning (RL) has substantially enhanced text- and vision-language models, while well-designed reward signals are crucial for the performance of RL. We consider RL a promising strategy to address the key challenge for SDMs. However, a fundamental barrier persists: prevailing automated metrics for assessing interaction quality rely on superficial proxies, such as behavioral statistics or timing-prediction accuracy, failing to provide reliable reward signals for RL. On the other hand, human evaluations, despite their richness, remain costly, inconsistent, and difficult to scale. We tackle this critical barrier by proposing a Dual-Axis Generative Reward Model, which is trained to understand complex interaction dynamics using a detailed taxonomy and an annotated dataset, produces a single score and, crucially, provides separate evaluations for semantic quality and interaction timing. Such dual outputs furnish precise diagnostic feedback for SDMs and deliver a dependable, instructive reward signal suitable for online reinforcement learning. Our model achieves state-of-the-art performance on interaction-quality assessment across a wide spectrum of datasets, spanning synthetic dialogues and complex real-world interactions.

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
