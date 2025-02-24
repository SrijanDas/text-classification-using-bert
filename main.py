import pandas as pd
import ktrain
from ktrain import text


data_train = pd.read_excel('data/train.xlsx', dtype=str)
data_test = pd.read_excel('data/test.xlsx', dtype=str)

print("Size of train dataset: ", data_train.shape)
print("Size of test dataset: ", data_test.shape)


(X_train, y_train), (X_test, y_test), preproc = text.texts_from_df(train_df=data_train,
                                                                   text_column='Reviews',
                                                                   label_columns='Sentiment',
                                                                   val_df=data_test,
                                                                   maxlen=500,
                                                                   preprocess_mode='bert')

model = text.text_classifier(name='bert', train_data=(X_train, y_train), preproc=preproc)

learner = ktrain.get_learner(model=model, train_data=(X_train, y_train), val_data=(X_test, y_test), batch_size=6)
learner.fit_onecycle(lr=2e-5, epochs=1)

predictor = ktrain.get_predictor(learner.model, preproc)
predictor.save('./bert')


data = ['this movie was horrible, the plot was really boring. acting was okay',
        'the film really sucked. there is not plot and acting was bad',
        'what a beautiful movie. great plot. acting was good. will see it again']

predictor.predict(data)
predictor.predict(data, return_proba=True)
