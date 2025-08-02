## ⚙️ Data
<p align="justify">
You can freely access the CQADupStack dataset through the following link:<br>
👉 http://nlp.cis.unimelb.edu.au/resources/cqadupstack/ <br><br>
Follow the instructions below to use the corresponding data for each component of the proposed system:<br>
</p>
  <ul> <h3> 1. Tag Diversity Preprocessing </h3>
<p align="justify">Extract questions and their corresponding tags from CQADupStack to handle tag diversity before performing user modeling.</p>
    <i>Example format:</i>
    
index | QuestionBody                                                                                                                   | tags
------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------
0     | i want to send files to android tablet with a application from pc...                                                           | usb connection mode
1     | i am playing around with my brand new motorola defy and trying to find a way to manage my contacts...                          | 2.2 froyo, contacts, dialer
  </ul>
  <ul> <h3> 2. Tag Generation </h3>
<p align="justify">Use the file named <code>User-Profiler (TrainData)</code> to train the tag generation component of the user knowledge profiler.
You may evaluate the model using <code>User-Profiler (TestData)</code>.</p>
    <i>Example format:</i>
    
| index | Question_ID | Forum_Name | User_ID | Question_Body                                                                                                                                       | Tags                         |
|-------|-------------|------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| 0     | 119926      | Unix       | 44686   | When I use "htop" command for linux (+F5), layout on 2 my vps different: Why on my first server I see broken tree?                                 | command-line terminal        |
| 1     | 41391       | English    | 10460   | If I want to mention the word "furlong", for example, should I use furlong, "furlong", or 'furlong'? Also, am I correct in putting the punctuation outside the quotes? | punctuation quotations italics |

</ul>
<ul> <h3> 3. User Modeling </h3>
<p align="justify">The file <code>UserHistory (TestData)</code> includes each user’s question history, allowing you to apply the fine-tuned model to generate user knowledge profiles based on past activity.</p>
    <i>Example format:</i>
    
index | userid | historyCount | historyIDs | history                                                                                       | forum
------|--------|--------------|------------|-----------------------------------------------------------------------------------------------|--------
0     | 44281  | 1            | 161862     | I need to reproduce the following plot...                                                     | Tex
1     | 210    | 2            | 1537, 685  | There is a shell command that allows to measure how ..., So recently a Debian ...             | Unix
</ul>
<ul> <h3> 4. Recognizing Question Entailment (RQE)</h3>
<p align="justify">Use the data named <code>Post-retrieval (TrainData)</code> to fine-tune your LLaMA-2 model for the RQE task. You may evaluate the model using <code>Post-retrieval (TestData)</code>.</p>
    <i>Example format:</i>
    
index | id_Q1 | id_Q2  | q1                                                         | q2                                      | ... | entailment | U_Background_kn
------|-------|--------|-------------------------------------------------------------|-----------------------------------------|-----|------------|-----------------
0     | 119926| 48033  | When I use htop command for linux...                        | Is there a graphic tool to add new...   | ... | Not-entailed | linux, bash...
1     | 41391 | 196200 | What is the best way to mention a word...                   | Should I use italics or quotes...       | ... | Entailed     | meaning, word...

<p align="justify">The data contains the following columns: <br>
<i>index</i> (row number), <i>id_Q1, id_Q2</i> (question IDs), <i>q1, q2</i> (RQE questions), <i>body_Q1, body_Q2</i> (full question texts), <i>forum_x, forum_y</i> (forum names of Q1 and Q2), <i>dups_Q1, dups_Q2</i> (duplicate question IDs), <i>tags_Q1, tags_Q2</i> (associated tags), <i>title_Q1, title_Q2</i> (question titles), <i>userid_Q1, userid_Q2</i> (user IDs), <i>entailment</i> (label: Entailed / Not-entailed), <i>U_Background_kn</i> (user_1 knowledge profile)
</p></ul>
<ul> <h3>5. Indexer</h3>
<p align="justify">Use the whole CQADupStack question bodies to be indexed by the indexer.</p>
    <i>Example format:</i>
    
| index | Dataset | QuestionID | QuestionBody                                       | viewcount | dups  | title                                               | tags                   | userid | related | score | answers   | acceptedanswer | creationdate           | favoritecount | comments       |
|-------|---------|------------|----------------------------------------------------|-----------|-------|------------------------------------------------------|------------------------|--------|---------|-------|-----------|----------------|------------------------|---------------|----------------|
| 99    | Android | 23508      | Aoson M19 tablet, can't find USB drivers...       | 666       | 23449 | Aoson M19 -- Device Drivers                          | usb-drivers            | 15384  | 23449   | -1    | 23509     | 23509          | 2012-05-25T14:51:57.187 | 0             | 27690 27691     |
| 154   | Android | 3742       | HTC released Froyo already on some phones...      | 207       | 2696  | Upgrade HTC Legend to Froyo without waiting?        | 2.2-froyo htc-legend   | 366    |         | 2     | 3744 4822 | 4822           | 2010-12-16T21:22:09.140 | 0             |                |


<p align="justify">The data contains columns named:<br>
<i>Dataset</i> (forum name), <i>QuestionID</i> (unique question identifier), <i>QuestionBody</i> (HTML-formatted question content), <i>viewcount</i> (number of times viewed), <i>dups</i> (duplicate question IDs), <i>title</i> (question title), <i>tags</i> (tab-separated tags), <i>userid</i> (ID of the user who posted), <i>related</i> (related question IDs), <i>score</i> (question score), <i>answers</i> (number of answers), <i>acceptedanswer</i> (ID of accepted answer), <i>creationdate</i> (timestamp of creation), <i>favoritecount</i> (number of times favorited), <i>comments</i> (comment IDs)
</p>
</ul>
<ul> <h3> 6. Retriever </h3>
<p align="justify">Use the data named <code>Generator GPT-4o (TestData)</code>. For each of the 148 questions in this dataset, compare it with each indexed question from the Indexer step.</p>
    <i>Example format:</i>
    
| index | Question_ID | Forum_Name  | User_ID | Question_Body                                           | Duplicate_Questions | Tags                          | Accepted_Answer_ID | Accepted_Answer_Body                                                                                                                |
|-------|-------------|-------------|---------|----------------------------------------------------------|---------------------|-------------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------|
| 0     | 113905      | English     | 44174   | Trying to find a programmer with who / whom to work...   | 56                  | word-choice grammaticality    | 113906             | "With whom" is correct, but most say: "a programmer that I can collaborate with."                                                 |
| 1     | 207196      | Programmers | 65453   | Confused about pointers in Java — do they exist or not?  | 141834 195337       | java pointers                 | 207225             | Java uses references which are pointer-like, but not in the C/C++ sense. It's a restricted, abstracted implementation detail.     |

</ul>

<ul> <h3> 7. Post-retrieval </h3>
<p align="justify">After retrieving the top-50 similar questions using the retriever, pass them to the fine-tuned RQE model as part of the post-retrieval process. Then, select the top-3 entailed questions based on their cosine similarity scores.</p>
</ul>

<ul>  <h3> 8. Generator </h3>
<p align="justify">The question bodies from the <code>Generator GPT-4o (TestData)</code> dataset, along with the top-3 entailed questions identified by the post-retrieval, are then passed to the Generator component.
</p></ul>

