# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-01-30 16:24:52 UTC
---

## Latest News

*No new papers matching your keywords found today.*


## Daily Recommendation

### 🌟 Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models

**Authors:** Matt Deitke, Christopher Clark, Sangho Lee et al.

**Conference:** CVPR.2025

**[Read Paper](/venue/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art@CVPR2025@CVF)**

Today's most advanced vision-language models (VLMs) remain proprietary. The strongest open-weight models rely heavily on synthetic data from proprietary VLMs to achieve good performance, effectively distilling these closed VLMs into open ones. As a result, the community has been missing foundational knowledge about how to build performant VLMs from scratch. We present \textbf{Molmo}, a new family of VLMs that are state-of-the-art in their class of openness. Our key contribution is a collection of new datasets, including a dataset of highly detailed image captions for pre-training called \textbf{PixMo}, a free-form image Q\&A dataset for fine-tuning, and an innovative 2D pointing dataset, all collected without the use of external VLMs. The success of our approach relies on careful modeling choices, a well-tuned training pipeline, and, most critically, the quality of our newly collected datasets. Our best-in-class 72B model not only outperforms others in the class of open weight and data models, but also outperforms larger proprietary models including Claude 3.5 Sonnet, and Gemini 1.5 Pro and Flash, second only to GPT-4o based on both academic benchmarks and on a large human evaluation. Our model weights, new datasets, and source code will all be released.

### 🌟 Identifying and Mitigating Position Bias of Multi-image Vision-Language Models

**Authors:** Xinyu Tian, Shu Zou, Zhaoyuan Yang et al.

**Conference:** CVPR.2025

**[Read Paper](/venue/Tian_Identifying_and_Mitigating_Position_Bias_of_Multi-image_Vision-Language_Models@CVPR2025@CVF)**

The evolution of Large Vision-Language Models (LVLMs) has progressed from single-image understanding to multi-image reasoning. Despite this advancement, our findings indicate that LVLMs struggle to robustly utilize information across multiple images, with predictions significantly affected by the alteration of image positions. To further explore this issue, we introduce Position-wise Question Answering (PQA), a meticulously designed task to quantify reasoning capabilities at each position. Our analysis reveals a pronounced position bias in LVLMs: open-source models excel in reasoning with images positioned later but underperform with those in the middle or at the beginning, while proprietary models like GPT-4o show improved comprehension for images at the beginning and end but struggle with those in the middle. Motivated by these insights, we propose SoFt Attention (SoFA), a simple, training-free approach that mitigates this bias by employing linear interpolation between inter-image causal attention and bidirectional counterparts. Experimental results demonstrate that SoFA effectively reduces position bias and significantly enhances the reasoning performance of existing LVLMs.

### 🌟 MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models

**Authors:** Peng Xia, Siwei Han, Shi Qiu et al.

**Conference:** ICLR.2025

**[Read Paper](/venue/HnhNRrLPwm@OpenReview)**

Interleaved multimodal comprehension and generation, enabling models to produce and interpret both images and text in arbitrary sequences, have become a pivotal area in multimodal learning. Despite significant advancements, the evaluation of this capability remains insufficient. Existing benchmarks suffer from limitations in data scale, scope, and evaluation depth, while current evaluation metrics are often costly or biased, lacking in reliability for practical applications. To address these challenges, we introduce MMIE, a large-scale knowledge-intensive benchmark for evaluating interleaved multimodal comprehension and generation in Large Vision-Language Models (LVLMs). MMIE comprises 20K meticulously curated multimodal queries, spanning 3 categories, 12 fields, and 102 subfields, including mathematics, coding, physics, literature, health, and arts. It supports both interleaved inputs and outputs, offering a mix of multiple-choice and open-ended question formats to evaluate diverse competencies. Moreover, we propose a reliable automated evaluation metric, leveraging a scoring model fine-tuned with human-annotated data and systematic evaluation criteria, aimed at reducing bias and improving evaluation accuracy. Extensive experiments demonstrate the effectiveness of our benchmark and metrics in providing a comprehensive evaluation of interleaved LVLMs. Specifically, we evaluate eight LVLMs, revealing that even the best models show significant room for improvement, with most achieving only moderate results. We believe MMIE will drive further advancements in the development of interleaved LVLMs.

---


## Weekly Summary

*Week ending 2026-01-30*

---

*No papers to summarize this week.*

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
