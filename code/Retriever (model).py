# -*- coding: utf-8 -*-
"""Retriever (Model).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UBGlp0usbUaQtj0ZTi2oBD1L7FzlLjgP
"""

cosine_sim_func = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
def get_top_k3_similar_questions(row, QArchiveQuestionsVect, ArchiveQuestions, k3):
    question_vector = ArchiveQuestionsVect[(ArchiveQuestions['Dataset']==row['forum_x']) &
                                           (ArchiveQuestions['QuestionID']==row['id_Q1'])]
    QSA = ArchiveQuestionsVect[(ArchiveQuestions['Dataset']==row['forum_x']) &
                               (ArchiveQuestions['QuestionID']!=row['id_Q1'])]
    cosine_sim = cosine_sim_func(question_vector, QSA)
    top_k3_indices = np.flip(np.argsort(cosine_sim.cpu())[-n:].numpy())
    top_k3_scores = np.flip(np.sort(cosine_sim.cpu())[-n:])
    similar_questions = (ArchiveQuestions[(ArchiveQuestions['Dataset']==row['forum_x']) &
                                          (ArchiveQuestions['QuestionID']!=row['id_Q1'])]).reset_index(drop=True).iloc[top_k3_indices]
    return top_k3_indices, top_k3_scores, similar_questions


def clean_text_list(text_list):
    combined_text = '###'.join(text_list)
    cleaned_text = re.sub(r'\s+', ' ', combined_text).strip()
    return cleaned_text.split('###')