<p align="justify">
<i><b>How do different indexers compare in terms of retrieval success rate? </i></b><br>
  To answer this, seven indexing methods are evaluated using Hit Ratio at k<sub>2</sub> (HR@k<sub>2</sub>), which measures the proportion of queries with at least one entailed question among the top-k<sub>2</sub> retrieved items (for k<sub>2</sub>∈{10,20,50}). Results are presented in Table 1, where the <i>all-mpnet-base-v2</i> model is identified as the best-performing indexer. Table 1 also reports the average time of generating vector representation of each archived question. 
</p>
<table border="0" cellspacing="0" cellpadding="6" align="center">
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th colspan="3">HR@k<sub>2</sub></th>
      <th rowspan="2">Average Time&nbsp;&uarr; (s)</th>
    </tr>
    <tr>
      <th>10</th>
      <th>20</th>
      <th>50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>bert-base-cased</b></td>
      <td>3</td><td>5</td><td>5</td>
      <td>2.89e-2</td>
    </tr>
    <tr>
      <td><b>unsup-simcse-roberta-base</b></td>
      <td>12</td><td>17</td><td>21</td>
      <td>1.71e-2</td>
    </tr>
    <tr>
      <td><b>tf-idf</b></td>
      <td>26</td><td>30</td><td>50</td>
      <td>1.03e-4</td>
    </tr>
    <tr>
      <td><b>paraphrase-minilm-l6-v2</b></td>
      <td>32</td><td>33</td><td>46</td>
      <td>9.63e-4</td>
    </tr>
    <tr>
      <td><b>paraphrase-multilingual-minilm-l12-v2</b></td>
      <td>38</td><td>42</td><td>47</td>
      <td>1.71e-3</td>
    </tr>
    <tr>
      <td><b>jina-colbert-v1-en</b></td>
      <td>40</td><td>47</td><td>60</td>
      <td>3.86e-3</td>
    </tr>
    <tr>
      <td><b>all-mpnet-base-v2</b></td>
      <td>72</td><td>80</td><td>95</td>
      <td>3.97e-2</td>
    </tr>
  </tbody>
</table>

<p align="center"> <b>Table 1: </b>Comparative Analysis of Indexing Methods </p>

<p align="justify">
<i><b>How effective is our proposed system in improving the quality of answers from various perspectives? </b></i><br>
A criterion-wise statistical comparison of the three systems is also provided in Table 10, including 95% confidence intervals and pairwise p-values calculated based on the average scores from six AI evaluators.
</p>
<table border="0" cellspacing="0" cellpadding="6" align="center">
  <thead>
    <tr>
      <th rowspan="2">Metric</th>
      <th colspan="3">AI Evaluator Scores (Mean ± CI)</th>
      <th colspan="3">p-value</th>
    </tr>
    <tr>
      <th>User-agnostic RAG</th>
      <th>Proposed system</th>
      <th>Pre-trained GPT-4o</th>
      <th>User-agnostic RAG vs Proposed</th>
      <th>Proposed vs GPT-4o</th>
      <th>User-agnostic RAG vs GPT-4o</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Hallucination</b></td>
      <td>3.9 ± 0.18</td>
      <td>4.4 ± 0.13</td>
      <td>4.5 ± 0.12</td>
      <td>1.4E-08</td>
      <td>5.3E-09</td>
      <td>3.9E-02</td>
    </tr>
    <tr>
      <td><b>Correctness</b></td>
      <td>3.3 ± 0.26</td>
      <td>4.1 ± 0.14</td>
      <td>4.3 ± 0.13</td>
      <td>1.8E-12</td>
      <td>8.7E-13</td>
      <td>5.8E-03</td>
    </tr>
    <tr>
      <td><b>Relevance</b></td>
      <td>3.5 ± 0.26</td>
      <td>4.4 ± 0.11</td>
      <td>4.6 ± 0.09</td>
      <td>1.1E-11</td>
      <td>5.7E-14</td>
      <td>6.6E-05</td>
    </tr>
    <tr>
      <td><b>Clarity & Conciseness</b></td>
      <td>3.3 ± 0.16</td>
      <td>4.0 ± 0.09</td>
      <td>4.6 ± 0.06</td>
      <td>2.8E-17</td>
      <td>3.7E-31</td>
      <td>2.3E-19</td>
    </tr>
    <tr>
      <td><b>Personalization</b></td>
      <td>2.6 ± 0.19</td>
      <td>3.2 ± 0.10</td>
      <td>3.5 ± 0.09</td>
      <td>1.0E-12</td>
      <td>2.0E-17</td>
      <td>1.6E-09</td>
    </tr>
    <tr>
      <td><b>Redundancy</b></td>
      <td>3.8 ± 0.09</td>
      <td>4.1 ± 0.08</td>
      <td>4.8 ± 0.04</td>
      <td>8.4E-09</td>
      <td>6.9E-38</td>
      <td>3.8E-28</td>
    </tr>
    <tr>
      <td><b>Complexity Appropriateness</b></td>
      <td>3.6 ± 0.23</td>
      <td>4.4 ± 0.08</td>
      <td>4.7 ± 0.06</td>
      <td>5.5E-10</td>
      <td>1.8E-14</td>
      <td>3.4E-09</td>
    </tr>
    <tr>
      <td><b>Completeness</b></td>
      <td>3.1 ± 0.24</td>
      <td>4.0 ± 0.12</td>
      <td>4.1 ± 0.10</td>
      <td>4.4E-14</td>
      <td>1.5E-12</td>
      <td>2.0E-02</td>
    </tr>
    <tr>
      <td><b>Depth & Detail</b></td>
      <td>3.2 ± 0.24</td>
      <td>4.0 ± 0.10</td>
      <td>4.0 ± 0.10</td>
      <td>4.2E-12</td>
      <td>3.6E-08</td>
      <td>4.1E-01</td>
    </tr>
    <tr>
      <td><b>Length Appropriateness</b></td>
      <td>3.4 ± 0.20</td>
      <td>4.2 ± 0.08</td>
      <td>4.8 ± 0.05</td>
      <td>2.9E-13</td>
      <td>3.4E-27</td>
      <td>5.1E-24</td>
    </tr>
    <tr>
      <td><b>Similarity to Gold Answer</b></td>
      <td>2.6 ± 0.21</td>
      <td>3.4 ± 0.14</td>
      <td>3.7 ± 0.13</td>
      <td>5.2E-17</td>
      <td>5.5E-18</td>
      <td>5.1E-04</td>
    </tr>
  </tbody>
</table>

<p align="center"><b>Table 2: </b>Statistical Analysis of Answer Generation Systems Based on Scores from Six AI Evaluators</p>

<p align="justify">
<i><b> Is the response time of the proposed system acceptable for practical deployment in Q&A communities? </b></i><br>
Although real-time responses are not expected in Q&A platforms, fast responses are still preferred. Table 3 reports the average processing time per user for each component, identifying the post-retrieval component as the main bottleneck. However, since retrieved questions can be assessed independently, parallelization is feasible, potentially reducing the delay to 0.36 seconds. Overall, the system delivers accurate and reliable responses in under 30 seconds.
</p>

<table border="0" cellspacing="0" cellpadding="6" align="center">
  <thead>
    <tr>
      <th>Component</th>
      <th>Time (s)</th>
      <th>Description</th>
      <th>Online</th>
      <th>GPU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>User profiler</b></td>
      <td>1.680</td>
      <td>Analyzing the 10 most recent questions of each user</td>
      <td>&#10007;</td>
      <td>A100</td>
    </tr>
    <tr>
      <td><b>Indexer</b></td>
      <td>0.014</td>
      <td>Representing the user's new question</td>
      <td>&#10003;</td>
      <td>T4</td>
    </tr>
    <tr>
      <td><b>Retriever</b></td>
      <td>0.602</td>
      <td>Retrieving the 50 most similar questions from 248,426 questions</td>
      <td>&#10003;</td>
      <td>T4</td>
    </tr>
    <tr>
      <td><b>Post-retrieval</b></td>
      <td>18.000</td>
      <td>Analyzing 50 question pairs sequentially</td>
      <td>&#10003;</td>
      <td>A100</td>
    </tr>
    <tr>
      <td><b>Generator</b></td>
      <td>5.660</td>
      <td>Prompting the GPT-4o to generate final answer</td>
      <td>&#10003;</td>
      <td>&mdash;</td>
    </tr>
  </tbody>
</table>

<p align="center"><b>Table 3: </b>Average Processing Time of the System Components per User</p>

