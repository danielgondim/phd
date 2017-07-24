focus_songs <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big.csv")
train <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big_train.csv")
test <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big_test.csv")

#com as variaveis independentes: voice_instrumental, acoustic e relaxed
model <- glm(focus ~ voice_instrumental_value+mood_acoustic_value+mood_relaxed_value,family=binomial(link='logit'),data=train)

summary(model)

anova(model, test="Chisq")

library(caret)


acc <- NULL
for(i in 1:nrow(focus_songs))
{
  # Train-test splitting
  # 499 samples -> fitting
  # 1 sample -> testing
  train <- focus_songs[-i,]
  test <- focus_songs[i,]
  
  # Fitting
  model <- glm(focus ~ voice_instrumental_value+mood_acoustic_value+mood_relaxed_value,family=binomial,data=train)
  
  # Predict results
  results_prob <- predict(model,newdata=test,type='response')
  
  # If prob > 0.5 then 1, else 0
  results <- ifelse(results_prob > 0.5,1,0)
  
  # Actual answers
  answers <- test$focus
  
  # Calculate accuracy
  misClasificError <- mean(answers != results)
  
  # Collecting results
  acc[i] <- 1-misClasificError
}

# Average accuracy of the model
mean(acc)

# Histogram of the model accuracy
hist(acc,xlab='Accuracy',ylab='Freq',main='Accuracy LOOCV',
     col='cyan',border='blue',density=30)

################################





# define training control
train_control<- trainControl(method="cv", number=10)

# train the model 
model_cv<- train(focus ~ voice_instrumental_value+mood_acoustic_value+mood_relaxed_value,
              data=focus_songs, trControl=train_control, method="glm", family=binomial(link='logit'))

# print cv scores
summary(model_cv)

library(pscl)
library(lattice)
library(ggplot2)
library(caret)

pR2(model)

pred <- predict(model, newdata=test)
pred <- ifelse(pred > 0.5,1,0)
accuracy <- table(pred, test[,"focus"])
sum(diag(accuracy))/sum(accuracy)

pred = predict(model, newdata=test)
confusionMatrix(data=pred, test$focus)

fitted.results <- predict(model,newdata=test,type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)
misClasificError <- mean(fitted.results != test$focus)
print(paste('Accuracy',1-misClasificError))

#com as variaveis independentes: voice_instrumental e relaxed
model2 <- glm(focus ~ voice_instrumental_value+mood_relaxed_value,family=binomial(link='logit'),data=train)

summary(model2)

fitted2.results <- predict(model2,newdata=test,type='response')
fitted2.results <- ifelse(fitted2.results > 0.5,1,0)
misClasificError2 <- mean(fitted2.results != test$focus)
print(paste('Accuracy',1-misClasificError2))

#com todas as variaveis independentes
model3 <- glm(focus ~ voice_instrumental_value+danceability_value+mood_acoustic_value+mood_aggressive_value+mood_party_value+mood_relaxed_value+tone+bpm,family=binomial(link='logit'),data=train)

summary(model3)

pR2(model3)

fitted.results3 <- predict(model3,newdata=test,type='response')
fitted.results3 <- ifelse(fitted.results3 > 0.5,1,0)
misClasificError3 <- mean(fitted.results3 != test$focus)
error <- sum(fitted.results3 != test$focus)
error
hits <- sum(fitted.results3 == test$focus)
hits
total <- nrow(test)
total

print(paste('Accuracy',1-misClasificError3))

#com as variaveis independentes: voice_instrumental e acoustic
model4 <- glm(focus ~ voice_instrumental_value+mood_acoustic_value,family=binomial(link='logit'),data=train)

summary(model4)

fitted.results4 <- predict(model4,newdata=test,type='response')
fitted.results4 <- ifelse(fitted.results4 > 0.5,1,0)
misClasificError4 <- sum(fitted.results4 != test$focus)
print(paste('Accuracy',1-misClasificError4))
