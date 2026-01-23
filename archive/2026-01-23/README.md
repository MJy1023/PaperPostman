# PaperPostman
> Automatically curated research papers from arXiv and papers.cool

**Last Updated:** 2026-01-23 17:52:04 UTC
---

## Latest News

*7 papers found matching your keywords.*

### 1. Multimodal Climate Disinformation Detection: Integrating Vision-Language Models with External Knowledge Sources

**Authors:** Marzieh Adeli Shamsabad, Hamed Ghodrati

**Published:** 2026-01-22

**Categories:** cs.AI

**[Read Paper](http://arxiv.org/abs/2601.16108v1)**

Climate disinformation has become a major challenge in today digital world, especially with the rise of misleading images and videos shared widely on social media. These false claims are often convincing and difficult to detect, which can delay actions on climate change. While vision-language models (VLMs) have been used to identify visual disinformation, they rely only on the knowledge available at the time of training. This limits their ability to reason about recent events or updates. The main goal of this paper is to overcome that limitation by combining VLMs with external knowledge. By retrieving up-to-date information such as reverse image results, online fact-checks, and trusted expert content, the system can better assess whether an image and its claim are accurate, misleading, false, or unverifiable. This approach improves the model ability to handle real-world climate disinformation and supports efforts to protect public understanding of science in a rapidly changing information landscape.

---

### 2. DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models

**Authors:** Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan et al.

**Published:** 2026-01-22

**Categories:** cs.CV, cs.RO

**[Read Paper](http://arxiv.org/abs/2601.16065v1)**

Vision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models (VLMs) to understand environments and directly output actions. However, by default, VLA models may overly attend to image tokens in the task-irrelevant region, which we describe as 'distracting tokens'. This behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tasks. In this paper, we introduce a simple yet effective plug-and-play Distracting Token Pruning (DTP) framework, which dynamically detects and prunes these distracting image tokens. By correcting the model's visual attention patterns, we aim to improve the task success rate, as well as exploring the performance upper boundaries of the model without altering its original architecture or adding additional inputs. Experiments on the SIMPLER Benchmark (Li et al., 2024) show that our method consistently achieving relative improvements in task success rates across different types of novel VLA models, demonstrating generalizability to transformer-based VLAs. Further analysis reveals a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region for all models tested, highlighting a common phenomenon of VLA models that could guide future research. We also publish our code at: https://anonymous.4open.science/r/CBD3.

---

### 3. DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning

**Authors:** Junha Lee, Eunha Park, Minsu Cho

**Published:** 2026-01-22

**Categories:** cs.RO, cs.CV

**[Read Paper](http://arxiv.org/abs/2601.16046v1)**

Language-driven dexterous grasp generation requires the models to understand task semantics, 3D geometry, and complex hand-object interactions. While vision-language models have been applied to this problem, existing approaches directly map observations to grasp parameters without intermediate reasoning about physical interactions. We present DextER, Dexterous Grasp Generation with Embodied Reasoning, which introduces contact-based embodied reasoning for multi-finger manipulation. Our key insight is that predicting which hand links contact where on the object surface provides an embodiment-aware intermediate representation bridging task semantics with physical constraints. DextER autoregressively generates embodied contact tokens specifying which finger links contact where on the object surface, followed by grasp tokens encoding the hand configuration. On DexGYS, DextER achieves 67.14% success rate, outperforming state-of-the-art by 3.83%p with 96.4% improvement in intention alignment. We also demonstrate steerable generation through partial contact specification, providing fine-grained control over grasp synthesis.

---

### 4. RadJEPA: Radiology Encoder for Chest X-Rays via Joint Embedding Predictive Architecture

**Authors:** Anas Anwarul Haq Khan, Mariam Husain, Kshitij Jadhav

**Published:** 2026-01-22

**Categories:** cs.CV

**[Read Paper](http://arxiv.org/abs/2601.15891v1)**

Recent advances in medical vision language models guide the learning of visual representations; however, this form of supervision is constrained by the availability of paired image text data, raising the question of whether robust radiology encoders can be learned without relying on language supervision. In this work, we introduce RadJEPA, a self-supervised framework built on a Joint Embedding Predictive Architecture that learns without language supervision. Pre-trained solely on unlabeled chest X-ray images, the model learns to predict latent representations of masked image regions. This predictive objective differs fundamentally from both image text pre-training and DINO-style self-distillation: rather than aligning global representations across views or modalities, RadJEPA explicitly models latent-space prediction. We evaluate the learned encoder on disease classification, semantic segmentation, and report generation tasks. Across benchmarks, RadJEPA achieves performance exceeding state-of-the-art approaches, including Rad-DINO.

---

### 5. Assessing Situational and Spatial Awareness of VLMs with Synthetically Generated Video

**Authors:** Pascal Benschop, Justin Dauwels, Jan van Gemert

**Published:** 2026-01-22

**Categories:** cs.CV

**[Read Paper](http://arxiv.org/abs/2601.15780v1)**

Spatial reasoning in vision language models (VLMs) remains fragile when semantics hinge on subtle temporal or geometric cues. We introduce a synthetic benchmark that probes two complementary skills: situational awareness (recognizing whether an interaction is harmful or benign) and spatial awareness (tracking who does what to whom, and reasoning about relative positions and motion). Through minimal video pairs, we test three challenges: distinguishing violence from benign activity, binding assailant roles across viewpoints, and judging fine-grained trajectory alignment. While we evaluate recent VLMs in a training-free setting, the benchmark is applicable to any video classification model. Results show performance only slightly above chance across tasks. A simple aid, stable color cues, partly reduces assailant role confusions but does not resolve the underlying weakness. By releasing data and code, we aim to provide reproducible diagnostics and seed exploration of lightweight spatial priors to complement large-scale pretraining.

---

### 6. Hallucination Mitigating for Medical Report Generation

**Authors:** Ruoqing Zhao, Runze Xia, Piji Li

**Published:** 2026-01-22

**Categories:** cs.CL

**[Read Paper](http://arxiv.org/abs/2601.15745v1)**

In the realm of medical report generation (MRG), the integration of natural language processing has emerged as a vital tool to alleviate the workload of radiologists. Despite the impressive capabilities demonstrated by large vision language models (LVLMs) in understanding natural language, their susceptibility to generating plausible yet inaccurate claims, known as ``hallucinations'', raises concerns-especially in the nuanced and critical field of medical. In this work, we introduce a framework, \textbf{K}nowledge-\textbf{E}nhanced with Fine-Grained \textbf{R}einforced Rewards \textbf{M}edical Report Generation (KERM), to tackle the issue. Our approach refines the input to the LVLM by first utilizing MedCLIP for knowledge retrieval, incorporating relevant lesion fact sentences from a curated knowledge corpus. We then introduce a novel purification module to ensure the retrieved knowledge is contextually relevant to the patient's clinical context. Subsequently, we employ fine-grained rewards to guide these models in generating highly supportive and clinically relevant descriptions, ensuring the alignment of model's outputs with desired behaviors. Experimental results on IU-Xray and MIMIC-CXR datasets validate the effectiveness of our approach in mitigating hallucinations and enhancing report quality.

---

### 7. Zero-Shot Product Attribute Labeling with Vision-Language Models: A Three-Tier Evaluation Framework

**Authors:** Shubham Shukla, Kunal Sonalkar

**Published:** 2026-01-22

**Categories:** cs.CV

**[Read Paper](http://arxiv.org/abs/2601.15711v1)**

Fine-grained attribute prediction is essential for fashion retail applications including catalog enrichment, visual search, and recommendation systems. Vision-Language Models (VLMs) offer zero-shot prediction without task-specific training, yet their systematic evaluation on multi-attribute fashion tasks remains underexplored. A key challenge is that fashion attributes are often conditional. For example, "outer fabric" is undefined when no outer garment is visible. This requires models to detect attribute applicability before attempting classification. We introduce a three-tier evaluation framework that decomposes this challenge: (1) overall task performance across all classes (including NA class: suggesting attribute is not applicable) for all attributes, (2) attribute applicability detection, and (3) fine-grained classification when attributes are determinable. Using DeepFashion-MultiModal, which explicitly defines NA (meaning attribute doesn't exist or is not visible) within attribute label spaces, we benchmark nine VLMs spanning flagship (GPT-5, Gemini 2.5 Pro), efficient (GPT-5 Mini, Gemini 2.5 Flash), and ultra-efficient tiers (GPT-5 Nano, Gemini 2.5 Flash-Lite) against classifiers trained on pretrained Fashion-CLIP embeddings on 5,000 images across 18 attributes. Our findings reveal that: (1) zero-shot VLMs achieve 64.0% macro-F1, a threefold improvement over logistic regression on pretrained Fashion-CLIP embeddings; (2) VLMs excel at fine-grained classification (Tier 3: 70.8% F1) but struggle with applicability detection (Tier 2: 34.1% NA-F1), identifying a key bottleneck; (3) efficient models achieve over 90% of flagship performance at lower cost, offering practical deployment paths. This diagnostic framework enables practitioners to pinpoint whether errors stem from visibility detection or classification, guiding targeted improvements for production systems.

---


## Daily Recommendation

### 🌟 MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models

**Authors:** Peng Xia, Siwei Han, Shi Qiu et al.

**Conference:** ICLR.2025

**[Read Paper](/venue/HnhNRrLPwm@OpenReview)**

Interleaved multimodal comprehension and generation, enabling models to produce and interpret both images and text in arbitrary sequences, have become a pivotal area in multimodal learning. Despite significant advancements, the evaluation of this capability remains insufficient. Existing benchmarks suffer from limitations in data scale, scope, and evaluation depth, while current evaluation metrics are often costly or biased, lacking in reliability for practical applications. To address these challenges, we introduce MMIE, a large-scale knowledge-intensive benchmark for evaluating interleaved multimodal comprehension and generation in Large Vision-Language Models (LVLMs). MMIE comprises 20K meticulously curated multimodal queries, spanning 3 categories, 12 fields, and 102 subfields, including mathematics, coding, physics, literature, health, and arts. It supports both interleaved inputs and outputs, offering a mix of multiple-choice and open-ended question formats to evaluate diverse competencies. Moreover, we propose a reliable automated evaluation metric, leveraging a scoring model fine-tuned with human-annotated data and systematic evaluation criteria, aimed at reducing bias and improving evaluation accuracy. Extensive experiments demonstrate the effectiveness of our benchmark and metrics in providing a comprehensive evaluation of interleaved LVLMs. Specifically, we evaluate eight LVLMs, revealing that even the best models show significant room for improvement, with most achieving only moderate results. We believe MMIE will drive further advancements in the development of interleaved LVLMs.

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

---


## Weekly Summary

*Week ending 2026-01-23*

---

*Summary generation skipped - LLM API not configured.*

---


---

*This repository is automatically maintained by PaperPostman.*
*Archived READMEs can be found in the [archive/](archive/) directory.*
