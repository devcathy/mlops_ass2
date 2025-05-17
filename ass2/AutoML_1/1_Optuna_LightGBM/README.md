# Summary of 1_Optuna_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 1553
- **learning_rate**: 0.1
- **feature_fraction**: 0.6372942274996019
- **bagging_fraction**: 0.649963737714838
- **min_data_in_leaf**: 2
- **metric**: binary_logloss
- **custom_eval_metric_name**: None
- **lambda_l1**: 0.00015613577890072756
- **lambda_l2**: 0.005003670155001035
- **bagging_freq**: 5
- **extra_trees**: True
- **num_boost_round**: 1000
- **early_stopping_rounds**: 50
- **cat_feature**: []
- **feature_pre_filter**: False
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 10
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

18.8 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.267532 | nan          |
| auc       | 0.953404 | nan          |
| f1        | 0.885605 |   0.543914   |
| accuracy  | 0.8955   |   0.543914   |
| precision | 1        |   0.982488   |
| recall    | 1        |   0.00240858 |
| mcc       | 0.791587 |   0.543914   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.267532 |  nan        |
| auc       | 0.953404 |  nan        |
| f1        | 0.885605 |    0.543914 |
| accuracy  | 0.8955   |    0.543914 |
| precision | 0.920364 |    0.543914 |
| recall    | 0.853376 |    0.543914 |
| mcc       | 0.791587 |    0.543914 |


## Confusion matrix (at threshold=0.543914)
|                          |   Predicted as Çerçevelik |   Predicted as Ürgüp Sivrisi |
|:-------------------------|--------------------------:|-----------------------------:|
| Labeled as Çerçevelik    |                       982 |                           70 |
| Labeled as Ürgüp Sivrisi |                       139 |                          809 |

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
