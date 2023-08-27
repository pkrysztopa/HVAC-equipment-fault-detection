import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def convert_date(date_str):
    return pd.to_datetime(date_str, format='%m/%d/%y')

def train_evaluate_classification_models(X_train, X_test, y_train, y_test, classifiers):
    # Dataframe to store the evaluation parameters.
    evaluation_df = pd.DataFrame(index=None, columns=['model','train_accuracy','test_accuracy','train_precision','test_precision',
                                        'train_recall','test_recall','train_f1','test_f1'])
    # List to store models
    models = []
    
    for mod in classifiers:
        name = mod[0]
        model = mod[1]

        model.fit(X_train,y_train)
        models.append(model)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        acc_train = accuracy_score(y_train, y_pred_train)
        acc_test = accuracy_score(y_test, y_pred_test)
        prec_train = precision_score(y_train, y_pred_train)
        prec_test = precision_score(y_test, y_pred_test)    
        rec_train = recall_score(y_train, y_pred_train)
        rec_test = recall_score(y_test, y_pred_test) 
        f1_train = f1_score(y_train, y_pred_train)
        f1_test = f1_score(y_test, y_pred_test)

        evaluation_df = evaluation_df.append(pd.Series({'model':name,
                                    'train_accuracy': acc_train,
                                    'test_accuracy': acc_test,
                                    'train_precision': prec_train,
                                    'test_precision': prec_test,
                                    'train_recall': rec_train,
                                    'test_recall': rec_test,
                                    'train_f1': f1_train,
                                    'test_f1': f1_test}),ignore_index=True)
    return models, evaluation_df

def train_evaluate_regression_models(X_train, X_test, y_train, y_test, regressors, models = []):
    # Dataframe to store the evaluation parameters.
    evaluation_df = pd.DataFrame(index=None, columns=['model','train_R2','test_R2','train_Mae','test_Mae','train_Mse','test_Mse'])
        
    for mod in regressors:
        name = mod[0]
        model = mod[1]

        model.fit(X_train, y_train)
        models.append(model)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        R2_train = r2_score(y_train, y_pred_train)
        R2_test = r2_score(y_test, y_pred_test)
        mae_train = mean_absolute_error(y_train, y_pred_train)
        mae_test = mean_absolute_error(y_test, y_pred_test)
        mse_train = mean_squared_error(y_train, y_pred_train)
        mse_test = mean_squared_error(y_test, y_pred_test)  
        evaluation_df = evaluation_df.append(pd.Series({'model':name, 
                                    'train_R2':R2_train,
                                    'test_R2':R2_test,
                                    'train_Mae':mae_train,
                                    'test_Mae':mae_test,
                                    'train_Mse':mse_train,
                                    'test_Mse':mse_test}),ignore_index=True )
    return models, evaluation_df