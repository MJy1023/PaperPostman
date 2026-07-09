# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-07-09 17:45:15 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models

**Authors:** Ruiqi Wang, Dezhong Zhao, Ziqin Yuan et al.

**Conference:** NeurIPS.2025

**[Read Paper](/venue/4xvE6Iy77Y@OpenReview)**

Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for teaching robots complex behaviors without reward engineering. However, its effectiveness is often limited by two critical challenges: the reliance on extensive human input and the inherent difficulties in resolving query ambiguity and credit assignment during reward learning. In this paper, we introduce PRIMT, a PbRL framework designed to overcome these challenges by leveraging foundation models (FMs) for multimodal synthetic feedback and trajectory synthesis. Unlike prior approaches that rely on single-modality FM evaluations, PRIMT employs a hierarchical neuro-symbolic fusion strategy, integrating the complementary strengths of vision-language models (VLMs) and large language models (LLMs) in evaluating robot behaviors for more reliable and comprehensive feedback. PRIMT also incorporates foresight trajectory generation to warm-start the trajectory buffer with bootstrapped samples, reducing early-stage query ambiguity, and hindsight trajectory augmentation for counterfactual reasoning with a causal auxiliary loss to improve credit assignment. We evaluate PRIMT on 2 locomotion and 6 manipulation tasks on various benchmarks, demonstrating superior performance over FM-based and scripted baselines. Website at https://primt25.github.io/.

### 🌟 The SA-FARI Dataset: Segment Anything in Footage of Animals for Recognition and Identification

**Authors:** Dante Wasmuht, Otto Brookes, Maximilian Schall et al.

**Conference:** CVPR.2026

**[Read Paper](/venue/Wasmuht_The_SA-FARI_Dataset_Segment_Anything_in_Footage_of_Animals_for@CVPR2026@CVF)**

Automated video analysis is critical for wildlife conservation. A foundational task in this domain is multi-animal tracking (MAT), which underpins applications such as individual re-identification and behavior recognition. However, existing datasets are limited in scale, constrained to a few species, or lack sufficient temporal and geographical diversity - leaving no suitable benchmark for training general-purpose MAT models applicable to wild animals. To address this, we introduce SA-FARI, the largest open-source MAT dataset for wild animals. It comprises 11,609 camera trap videos collected over 10 years (2014-2024) from 741 locations across 4 continents, spanning 99 species categories. Each video is exhaustively annotated culminating in 46 hours of densely annotated footage containing 16,224 masklet identities and 942,702 individual bounding boxes, segmentation masks, and species labels. Alongside the task-specific annotations, we publish anonymized camera trap locations for each video. Finally, we present comprehensive benchmarks on SA-FARI using state-of-the-art vision-language models for detection and tracking, including SAM 3, evaluated with both species-specific and generic animal prompts. We also compare against vision only methods developed specifically for wildlife analysis. SA-FARI is the first large-scale dataset to combine high species diversity, multi-region coverage, and high-quality spatio-temporal annotations, offering a new foundation for advancing multi-animal tracking in the wild. The dataset is available at conservationxlabs.com/SA-FARI.

### 🌟 Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

**Authors:** Chufan Shi, Cheng Yang, Yaokang Wu et al.

**Conference:** ICML.2026

**[Read Paper](/venue/DdU1o2ZvWi@OpenReview)**

Vision-Language Models (VLMs) often produce self-reflective statements like “let me check the figure again” during reasoning. Do such state- ments trigger genuine visual re-examination, or are they merely learned textual patterns? We in- vestigate this via VISUALSWAP, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-BENCH, 800 image pairs curated from MathVista, Math- Verse, MathVision, and MMMU-Pro. Exper- iments on Qwen3-VL, Kimi-VL, and ERNIE- VL reveal a striking failure: models overwhelm- ingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking mod- els are nearly 3x more vulnerable than their in- structed counterparts, and scaling offers no mit- igation. Multi-turn user instructions restore vi- sual grounding, but self-generated reflective state- ments during continuous generation do not. At- tention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io/

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
