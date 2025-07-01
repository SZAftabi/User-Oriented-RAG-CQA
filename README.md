![GitHub Repo](https://img.shields.io/badge/Research-Paper-blue)
# **Enhancing Reliability in Community Question Answering with an Expert-Oriented RAG System**
## 📜 Abstract
<p align="justify">
In recent years, pre-trained large language models (LLMs) have become a cornerstone for automatically generating answers in question-and-answer (Q&A) communities, significantly reducing user wait times and improving response quality. However, these models require substantial computational resources and are prone to generating hallucinated or unreliable content. To overcome these limitations, we propose an advanced export-oriented Retrieval-Augmented Generation (RAG) framework as a cost-effective and reliable alternative. Central to our approach is a user-aware question entailment recognition module, which leverages user modeling to identify archived questions with answers that fully or partially address the user's new query. This user modeling significantly improves retrieval relevance, resulting in reduced hallucination and enhanced answer quality. The framework synthesizes expert-written answers from similar questions to generate unified responses. Experimental results on the CQADupStack dataset show that our user-aware approach achieves a 3.6% improvement in ROUGE-1 over its user-agnostic counterpart. Both human and AI evaluations confirm the effectiveness of incorporating user modeling in minimizing hallucination and delivering high-quality, contextually appropriate answers—demonstrating its potential for real-world Q&A systems. 
</p>
<p align="center"><img src="ProposedSystem.jpg" width="700" alt="ProposedFramework"></p>
<p align="center"><b> Fig 1. </b> Overview of the advanced knowledge- and retrieval- augmented generation-based community question answering system </p>

## ⚙️ Data
<p align="justify">
You can freely access the CQADupStack dataset through the following link:<br>
👉 http://nlp.cis.unimelb.edu.au/resources/cqadupstack/ <br><br>
Follow the instructions below to use the corresponding data for each component of the proposed system:<br>
  <ul> <h3> 1. Tag Diversity Preprocessing </h3>
Extract questions and their corresponding tags from CQADupStack to handle tag diversity before performing user modeling.
  </ul>
  <ul> <h3> 2. Tag Generation </h3>
Use the file named <code>User-Profiler (TrainData)</code> to train the tag generation component of the user knowledge profiler.
You may evaluate the model using <code>User-Profiler (TestData)</code>.

<br><i>Example format:</i>
index | QuestionBody                                                                                                                   | tags
------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------
0     | i want to send files to android tablet with a application from pc...                                                           | usb connection mode
1     | i am playing around with my brand new motorola defy and trying to find a way to manage my contacts...                          | 2.2 froyo, contacts, dialer
</ul>
<ul> <h3> 3. User Modeling </h3>
The file <code>UserHistory (TestData)</code>code> includes each user’s question history, allowing you to apply the fine-tuned model to generate user knowledge profiles based on past activity.

<br><i>Example format:</i>
index | userid | historyCount | historyIDs | history                                                                                       | forum
------|--------|--------------|------------|-----------------------------------------------------------------------------------------------|--------
0     | 44281  | 1            | 161862     | I need to reproduce the following plot...                                                     | Tex
1     | 210    | 2            | 1537, 685  | There is a shell command that allows to measure how ..., So recently a Debian ...             | Unix
</ul>
