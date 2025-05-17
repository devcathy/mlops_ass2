# Summary of 2_Optuna_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eta**: 0.05
- **max_depth**: 5
- **min_child_weight**: 1
- **subsample**: 0.5758258292131195
- **colsample_bytree**: 0.3228568309919116
- **eval_metric**: logloss
- **lambda**: 1.4668648312244355e-06
- **alpha**: 8.22322663436197e-07
- **max_rounds**: 1000
- **early_stopping_rounds**: 50
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 10
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

16.4 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.271852 | nan          |
| auc       | 0.952193 | nan          |
| f1        | 0.884842 |   0.442869   |
| accuracy  | 0.8925   |   0.442869   |
| precision | 1        |   0.991096   |
| recall    | 1        |   0.00262342 |
| mcc       | 0.784423 |   0.442869   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.271852 |  nan        |
| auc       | 0.952193 |  nan        |
| f1        | 0.884842 |    0.442869 |
| accuracy  | 0.8925   |    0.442869 |
| precision | 0.898803 |    0.442869 |
| recall    | 0.871308 |    0.442869 |
| mcc       | 0.784423 |    0.442869 |


## Confusion matrix (at threshold=0.442869)
|                          |   Predicted as Çerçevelik |   Predicted as Ürgüp Sivrisi |
|:-------------------------|--------------------------:|-----------------------------:|
| Labeled as Çerçevelik    |                       959 |                           93 |
| Labeled as Ürgüp Sivrisi |                       122 |                          826 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)
### Dependence (Fold 2)
![SHAP Dependence from Fold 2](learner_fold_1_shap_dependence.png)
### Dependence (Fold 3)
![SHAP Dependence from Fold 3](learner_fold_2_shap_dependence.png)
### Dependence (Fold 4)
![SHAP Dependence from Fold 4](learner_fold_3_shap_dependence.png)
### Dependence (Fold 5)
![SHAP Dependence from Fold 5](learner_fold_4_shap_dependence.png)
### Dependence (Fold 6)
![SHAP Dependence from Fold 6](learner_fold_5_shap_dependence.png)
### Dependence (Fold 7)
![SHAP Dependence from Fold 7](learner_fold_6_shap_dependence.png)
### Dependence (Fold 8)
![SHAP Dependence from Fold 8](learner_fold_7_shap_dependence.png)
### Dependence (Fold 9)
![SHAP Dependence from Fold 9](learner_fold_8_shap_dependence.png)
### Dependence (Fold 10)
![SHAP Dependence from Fold 10](learner_fold_9_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 2)
![SHAP worst decisions class 0 from Fold 2](learner_fold_1_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 3)
![SHAP worst decisions class 0 from Fold 3](learner_fold_2_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 4)
![SHAP worst decisions class 0 from Fold 4](learner_fold_3_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 5)
![SHAP worst decisions class 0 from Fold 5](learner_fold_4_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 6)
![SHAP worst decisions class 0 from Fold 6](learner_fold_5_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 7)
![SHAP worst decisions class 0 from Fold 7](learner_fold_6_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 8)
![SHAP worst decisions class 0 from Fold 8](learner_fold_7_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 9)
![SHAP worst decisions class 0 from Fold 9](learner_fold_8_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold 10)
![SHAP worst decisions class 0 from Fold 10](learner_fold_9_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 2)
![SHAP best decisions class 0 from Fold 2](learner_fold_1_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 3)
![SHAP best decisions class 0 from Fold 3](learner_fold_2_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 4)
![SHAP best decisions class 0 from Fold 4](learner_fold_3_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 5)
![SHAP best decisions class 0 from Fold 5](learner_fold_4_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 6)
![SHAP best decisions class 0 from Fold 6](learner_fold_5_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 7)
![SHAP best decisions class 0 from Fold 7](learner_fold_6_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 8)
![SHAP best decisions class 0 from Fold 8](learner_fold_7_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 9)
![SHAP best decisions class 0 from Fold 9](learner_fold_8_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold 10)
![SHAP best decisions class 0 from Fold 10](learner_fold_9_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 2)
![SHAP worst decisions class 1 from Fold 2](learner_fold_1_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 3)
![SHAP worst decisions class 1 from Fold 3](learner_fold_2_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 4)
![SHAP worst decisions class 1 from Fold 4](learner_fold_3_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 5)
![SHAP worst decisions class 1 from Fold 5](learner_fold_4_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 6)
![SHAP worst decisions class 1 from Fold 6](learner_fold_5_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 7)
![SHAP worst decisions class 1 from Fold 7](learner_fold_6_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 8)
![SHAP worst decisions class 1 from Fold 8](learner_fold_7_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 9)
![SHAP worst decisions class 1 from Fold 9](learner_fold_8_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 10)
![SHAP worst decisions class 1 from Fold 10](learner_fold_9_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 2)
![SHAP best decisions class 1 from Fold 2](learner_fold_1_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 3)
![SHAP best decisions class 1 from Fold 3](learner_fold_2_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 4)
![SHAP best decisions class 1 from Fold 4](learner_fold_3_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 5)
![SHAP best decisions class 1 from Fold 5](learner_fold_4_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 6)
![SHAP best decisions class 1 from Fold 6](learner_fold_5_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 7)
![SHAP best decisions class 1 from Fold 7](learner_fold_6_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 8)
![SHAP best decisions class 1 from Fold 8](learner_fold_7_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 9)
![SHAP best decisions class 1 from Fold 9](learner_fold_8_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold 10)
![SHAP best decisions class 1 from Fold 10](learner_fold_9_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
