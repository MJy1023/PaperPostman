# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-08-17 16:13:04 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

**Authors:** Chufan Shi, Cheng Yang, Yaokang Wu et al.

**Conference:** ICML.2026

**[Read Paper](/venue/DdU1o2ZvWi@OpenReview)**

Vision-Language Models (VLMs) often produce self-reflective statements like “let me check the figure again” during reasoning. Do such state- ments trigger genuine visual re-examination, or are they merely learned textual patterns? We in- vestigate this via VISUALSWAP, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-BENCH, 800 image pairs curated from MathVista, Math- Verse, MathVision, and MMMU-Pro. Exper- iments on Qwen3-VL, Kimi-VL, and ERNIE- VL reveal a striking failure: models overwhelm- ingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking mod- els are nearly 3x more vulnerable than their in- structed counterparts, and scaling offers no mit- igation. Multi-turn user instructions restore vi- sual grounding, but self-generated reflective state- ments during continuous generation do not. At- tention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io/

### 🌟 The SA-FARI Dataset: Segment Anything in Footage of Animals for Recognition and Identification

**Authors:** Dante Wasmuht, Otto Brookes, Maximilian Schall et al.

**Conference:** CVPR.2026

**[Read Paper](/venue/Wasmuht_The_SA-FARI_Dataset_Segment_Anything_in_Footage_of_Animals_for@CVPR2026@CVF)**

Automated video analysis is critical for wildlife conservation. A foundational task in this domain is multi-animal tracking (MAT), which underpins applications such as individual re-identification and behavior recognition. However, existing datasets are limited in scale, constrained to a few species, or lack sufficient temporal and geographical diversity - leaving no suitable benchmark for training general-purpose MAT models applicable to wild animals. To address this, we introduce SA-FARI, the largest open-source MAT dataset for wild animals. It comprises 11,609 camera trap videos collected over 10 years (2014-2024) from 741 locations across 4 continents, spanning 99 species categories. Each video is exhaustively annotated culminating in 46 hours of densely annotated footage containing 16,224 masklet identities and 942,702 individual bounding boxes, segmentation masks, and species labels. Alongside the task-specific annotations, we publish anonymized camera trap locations for each video. Finally, we present comprehensive benchmarks on SA-FARI using state-of-the-art vision-language models for detection and tracking, including SAM 3, evaluated with both species-specific and generic animal prompts. We also compare against vision only methods developed specifically for wildlife analysis. SA-FARI is the first large-scale dataset to combine high species diversity, multi-region coverage, and high-quality spatio-temporal annotations, offering a new foundation for advancing multi-animal tracking in the wild. The dataset is available at conservationxlabs.com/SA-FARI.

### 🌟 Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models

**Authors:** Yifu Chen, Shengpeng Ji, Zhengqing Liu et al.

**Conference:** ACL.2026

**[Read Paper](/venue/2026.acl-long.6@ACL)**

Achieving seamless, human-like interaction remains a key challenge for full-duplex spoken dialogue models (SDMs). Reinforcement learning (RL) has substantially enhanced text- and vision-language models, while well-designed reward signals are crucial for the performance of RL. We consider RL a promising strategy to address the key challenge for SDMs. However, a fundamental barrier persists: prevailing automated metrics for assessing interaction quality rely on superficial proxies, such as behavioral statistics or timing-prediction accuracy, failing to provide reliable reward signals for RL. On the other hand, human evaluations, despite their richness, remain costly, inconsistent, and difficult to scale. We tackle this critical barrier by proposing a Dual-Axis Generative Reward Model, which is trained to understand complex interaction dynamics using a detailed taxonomy and an annotated dataset, produces a single score and, crucially, provides separate evaluations for semantic quality and interaction timing. Such dual outputs furnish precise diagnostic feedback for SDMs and deliver a dependable, instructive reward signal suitable for online reinforcement learning. Our model achieves state-of-the-art performance on interaction-quality assessment across a wide spectrum of datasets, spanning synthetic dialogues and complex real-world interactions.

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
