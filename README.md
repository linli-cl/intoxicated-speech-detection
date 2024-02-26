# TeamLab_LiYen
Alcohol consumption causes numerous servere social, psychologial, and health problems including an increase in traffic accidents. Successful identification of alcohol consumption is crucial in addressing and preventing drinking and driving, as well as other safety and security issues. Using the Alcohol Language Corpus, the project’s task is designed as a binary classification between sober and drunk speech. This project attempts to use different feature kinds from raw speech and different machine learning/deep learning models to detect intoxicated speech. For each model, diverse techniques are applied such as oversampling, permutation importance for random forest, focal loss for convolutional neural network, memory-efficient tricks for pretrained model to achieve the best performance.

This directory contains following contents(partial):

- BiLSTM: The directory containing the BiLSTM run files mentioned in the report and the model parameter files used for testing.
    - BiLSTM_original_data.ipynb: The bilstm model trained with original unbalanced data and run records.
    - BiLSTM_reload_results.ipynb: Evaluate the code and test both models on a test set. Evaluations include: accuracy, confusion matrix and speech styles.
    - model-bilstm-all.ph: The bilstm model trained with original unbalanced data.
    - model-oversampling.ph: The bilstm model trained with oversampling balanced data.
  
- random_forest.ipynb: Code and run logs for the random forest method mentioned in the report. Includes training of the random forest, feature selection and evaluation of the three forests.
                         
- README.txt: This file.

- Please see "report_intoxicated Speech Detection.pdf" for a detailed description of the project.
