---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Have a nice day! 😊

---

I am a second-year M.Eng. student at [Tsinghua University](https://www.tsinghua.edu.cn/en/). Before that, I received my B.Eng. degree in Software Engineering from [Jilin University](https://www.jlu.edu.cn/) in 2024.

<br>

My research centers on **Large Language Models (LLMs)**, with a focus on code intelligence (generation, understanding, and vulnerability detection), long-context compression, and inference efficiency. I also have experience in **Data Mining** (user behavior modeling, recommendation systems) and **Computer Networks** (failure localization, intelligent routing). I am broadly interested in building reliable and efficient LLM systems that bridge natural language, code, and structured data.

I have published papers at top venues including EMNLP, KDD, AAMAS, and Computer Networks. <a href='https://scholar.google.com.hk/citations?user=YKSeHjsAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>


# 🔥 News
- *2026.03*: &nbsp;🎉🎉 "Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety" is accepted by **ICMR 2026**! See you in Amsterdam! 🇳🇱
- *2025.09*: &nbsp;🎉🎉 "SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design" is accepted by **EMNLP 2025 (Oral)**! See you in Suzhou! 🇨🇳
- *2024.05*: &nbsp;🎉🎉 "Make Your Home Safe: Time-aware Unsupervised User Behavior Anomaly Detection in Smart Homes via Loss-guided Mask" is accepted by **KDD 2024**! See you in Barcelona! 🇪🇸
- *2024.01*: &nbsp;🎉🎉 "Themis: A passive-active hybrid framework with in-network intelligence for lightweight failure localization" is accepted by **Computer Networks 2024**!
- *2023.01*: &nbsp;🎉🎉 "User Device Interaction Prediction via Relational Gated Graph Attention Network and Intent-aware Encoder" is accepted by **AAMAS 2023**! See you in London! 🇬🇧

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Oral</div><img src='images/slidecoder.png' alt="SlideCoder" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design](https://arxiv.org/abs/2506.07964)

**Wenxin Tang**, Jingyu Xiao, Xi Xiao, Wenxuan Jiang, Yuhang Wang, Qing Li, Xuxin Tang, Yuehe Ma, Junliang Liu, Shisong Tang, Michael R. Lyu. **EMNLP 2025 (Oral)**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/efficientpostergen.png' alt="EfficientPosterGen" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EfficientPosterGen: Information Density-aware Retrieval and Token Compression for Efficient Academic Poster Generation](https://arxiv.org/abs/2603.00155)

**Wenxin Tang**, Jingyu Xiao, Yanpei Gong, Fengyuan Ran, Tongchuan Xia, Junliang Liu, Man Ho Lam, Wenxuan Wang, Michael R. Lyu. **Under Review**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/dcvd.png' alt="DCVD" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization](https://arxiv.org/abs/2605.11015)

**Wenxin Tang**, Wenbin Li, Junliang Liu, Jingyu Xiao, Xi Xiao, Mingzhe Liu, Jinlong Yang, Xuan Liu, Yuehe Ma, Wang Luo, Qing Li, Lei Wang, Peng Xiangli. *Preprint*
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/vultriage.png' alt="VulTriage" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection](https://arxiv.org/abs/2605.09461)

**Wenxin Tang**, Xiang Zhang, Junliang Liu, Jingyu Xiao, Xi Xiao, Jinlong Yang, Yuehe Ma, Zhenyu Liu, Zhengheng Li, Zicheng Wang, Wang Luo, Qing Li, Lei Wang, Peng Xiangli. *Preprint*
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICMR 2026</div><img src='images/webpai.png' alt="WebPAI" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety](https://arxiv.org/abs/2509.21782)

Junliang Liu, Jingyu Xiao, **Wenxin Tang**, Zhixian Wang, Zipeng Xie, Wenxuan Wang, Minrui Zhang, Shuanghe Yu. **ICMR 2026**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2024</div><img src='images/kdd2024.png' alt="KDD2024" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Make Your Home Safe: Time-aware Unsupervised User Behavior Anomaly Detection in Smart Homes via Loss-guided Mask](https://dl.acm.org/doi/10.1145/3637528.3671708)

Jingyu Xiao, Zhiyao Xu, Qingsong Zou, Qing Li, Dan Zhao, Dong Fang, Ruoyu Li, **Wenxin Tang**, Kang Li, Xudong Zuo, Penghui Hu, Yong Jiang, Zixuan Weng, Michael R. Lyu. **KDD 2024**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAMAS 2023</div><img src='images/aamas2023.png' alt="AAMAS2023" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[User Device Interaction Prediction via Relational Gated Graph Attention Network and Intent-aware Encoder](https://whalexiao.github.io/publications/AAMAS_2023_DeepUDI_Xiao.pdf)

Jingyu Xiao, Qingsong Zou, Qing Li, Dan Zhao, Kang Li, **Wenxin Tang**, Runjie Zhou, Yong Jiang. **AAMAS 2023**
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Computer Networks 2024</div><img src='images/themis.png' alt="Themis" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Themis: A passive-active hybrid framework with in-network intelligence for lightweight failure localization](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4604412)

Qing Li, Jingyu Xiao, Dan Zhao, Xudong Zuo, **Wenxin Tang**, Yong Jiang. **Computer Networks 2024**
</div>
</div>

# 🧑‍💻 Internships

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tencent</div><img src='images/tencent.png' alt="Tencent" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[WeChat Group](https://www.wechat.com/en) (WXG)

**Video Platform Department, Research Intern**

Participated in injecting world knowledge and reasoning capabilities of LLMs into the full pipeline of recommendation systems (LLM4Rec). Built cross-domain intent models using LLMs for user profiling and latent interest mining, applied to downstream U2I tasks to support routine inference for hundreds of millions of users. Also participated in constructing multimodal embeddings from live-streaming data using RQKMeans clustering to enhance live-streaming ID representations.

*2025.01 - Present, Shenzhen, China*
</div>
</div>

# 🎖 Honors and Awards
- *2021* **National Scholarship**, Ministry of Education of China (**Top 1.7%**)
- *2025* Second Class Scholarship, Tsinghua University
- *2022* Second Class Scholarship, Jilin University (Top 15%)
- *2020, 2021, 2022* Outstanding Student, Jilin University (Top 5%)
- *2020* First Class Scholarship, Jilin University (Top 5%)

# 📖 Educations
- *2024.09 - 2027.06 (Expected)*, M.Eng. in Computer Technology, **Tsinghua University** (Recommended for Admission), GPA: 3.7/4.0
- *2019.09 - 2024.06*, B.Eng. in Software Engineering, **Jilin University**, GPA: 3.66/4.0

# 💼 Academic Service
- Sub-reviewer: KDD 2026
- Conference Volunteer: EMNLP 2025
