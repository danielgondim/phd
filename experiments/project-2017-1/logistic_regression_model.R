focus_songs <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big.csv")
train <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big_train.csv")
test <- read.csv("/home/danielgondim/workspace-new/phd/experiments/project-2017-1/songs_with_features_reduced_big_test.csv")

#com as variaveis independentes: voice_instrumental, acoustic e relaxed
model <- glm(focus ~ voice_instrumental_value+mood_acoustic_value+mood_relaxed_value,family=binomial(link='logit'),data=train)

summary(model)

anova(model, test="Chisq")

library(pscl)
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
print(paste('Accuracy',1-misClasificError3))

#com as variaveis independentes: voice_instrumental e acoustic
model4 <- glm(focus ~ voice_instrumental_value+mood_acoustic_value,family=binomial(link='logit'),data=train)

summary(model4)

fitted.results4 <- predict(model4,newdata=test,type='response')
fitted.results4 <- ifelse(fitted.results4 > 0.5,1,0)
misClasificError4 <- mean(fitted.results4 != test$focus)
print(paste('Accuracy',1-misClasificError4))
