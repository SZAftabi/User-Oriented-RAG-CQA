![GitHub Repo](https://img.shields.io/badge/Research-Paper-blue)
# **Experimental results on a selection subset of SE-PQA dataset, matched in size to the research test dataset**
## 
<p align="justify">
    
<table border="0" cellspacing="0" cellpadding="6" align="center">
  <thead>
    <tr>
      <th>Metric</th>
      <th>BERTScore</th>
      <th>ROUGE-1</th>
      <th>ROUGE-2</th>
      <th>ROUGE-L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Recall-based</b></td>
      <td>1.000</td>
      <td>0.999</td>
      <td>0.998</td>
      <td>0.999</td>
    </tr>
    <tr>
      <td><b>Precision-based</b></td>
      <td>1.000</td>
      <td>0.999</td>
      <td>0.997</td>
      <td>0.999</td>
    </tr>
    <tr>
      <td><b>F1-based</b></td>
      <td>1.000</td>
      <td>0.999</td>
      <td>0.997</td>
      <td>0.999</td>
    </tr>
  </tbody>
</table>

<p align="center"><b> Table 1: </b> Performance Evaluation of LLaMA-2 for Tag Generation on SE-PQA-Based Test Data </p>

<br>
<table border="0" cellspacing="0" cellpadding="6" align= "center">
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="2">ROUGE-1</th>
      <th colspan="2">ROUGE-2</th>
      <th colspan="2">ROUGE-L</th>
      <th colspan="2">BERTScore</th>
      <th rowspan="2">BLEU-1</th>
      <th rowspan="2">BLEU-2</th>
      <th rowspan="2">METEOR</th>
      <th rowspan="2">Perplexity</th>
    </tr>
    <tr>
      <th>F1</th><th>Re</th>
      <th>F1</th><th>Re</th>
      <th>F1</th><th>Re</th>
      <th>F1</th><th>Re</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>User-agnostic RAG</b></td>
      <td>28.7</td><td>39.4</td>
      <td>6.3</td><td>8.6</td>
      <td>14.6</td><td>21.5</td>
      <td>83.2</td><td>83.4</td>
      <td>17.9</td><td>7.4</td><td>18.5</td><td>31.00</td>
    </tr>
    <tr>
      <td><b>User-aware RAG (ours)</b></td>
      <td>29.6</td><td>42.2</td>
      <td>6.6</td><td>9.6</td>
      <td>14.8</td><td>22.7</td>
      <td>83.2</td><td>83.7</td>
      <td>18.5</td><td>7.7</td><td>19.1</td><td>32.30</td>
    </tr>
    <tr>
      <td><b>Pre-trained GPT-4o</b></td>
      <td>27.9</td><td>35.0</td>
      <td>5.7</td><td>7.5</td>
      <td>14.5</td><td>19.6</td>
      <td>83.1</td><td>83.2</td>
      <td>15.8</td><td>6.2</td><td>15.9</td><td>39.27</td>
    </tr>
      <tr>
          <td colspan="13"><b>F1</b>: F1-based  <b>Re</b>: Recall-based</td>
      </tr>
  </tbody>
</table>


<p align="center"><b> Table 2: </b> Quantitative Analysis of User-Aware RAG vs. User-Agnostic RAG and Pre-trained GPT-4o on SE-PQA-Based Test Data </p>

</p>
