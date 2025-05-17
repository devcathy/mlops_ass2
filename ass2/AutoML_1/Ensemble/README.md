# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                 |   Weight |
|:----------------------|---------:|
| 1_Optuna_LightGBM     |        1 |
| 2_Optuna_Xgboost      |        1 |
| 3_Optuna_RandomForest |        1 |

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.264678 | nan          |
| auc       | 0.954611 | nan          |
| f1        | 0.888056 |   0.45137    |
| accuracy  | 0.8955   |   0.45137    |
| precision | 1        |   0.980023   |
| recall    | 1        |   0.00364726 |
| mcc       | 0.790857 |   0.495641   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.264678 |   nan       |
| auc       | 0.954611 |   nan       |
| f1        | 0.888056 |     0.45137 |
| accuracy  | 0.8955   |     0.45137 |
| precision | 0.902067 |     0.45137 |
| recall    | 0.874473 |     0.45137 |
| mcc       | 0.790451 |     0.45137 |


## Confusion matrix (at threshold=0.45137)
|                          |   Predicted as Çerçevelik |   Predicted as Ürgüp Sivrisi |
|:-------------------------|--------------------------:|-----------------------------:|
| Labeled as Çerçevelik    |                       962 |                           90 |
| Labeled as Ürgüp Sivrisi |                       119 |                          829 |

## Learning curves
![Learning curves](learning_curves.png)
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



[<< Go back](../README.md)
