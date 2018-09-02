library(forecast)
df3<-austres
plot(df3)
plot(decompose(df3))

dcp <- decompose(df3)
dcp$trend
dcp$seasonal
df <- data("taylor")
df <- taylor

plot(df)

plot(decompose(df))

df2 <- AirPassengers
plot(df2)
plot(decompose(df2))


plot(meanf(df3,h=10))
plot(naive(df3,h=10))
plot(snaive(df3,h=10))
plot(rwf(df3,drift = T,h=10))


fit1 <- ses(df3)
fcast1 <- forecast(fit1,h=10)
plot(fcast1)


fit <- HoltWinters(df3)
fcast <- forecast(fit,h=10)
plot(fcast)
fcast
summary(fit)
summary(fit1)


library(jsonlite)

data <- fromJSON("https://exactspace.co/sensordata/profile1")
plot(data$temperature,type="l")

data$date = as.POSIXct(data$time/1000,origin="1970-01-01", tz = 'GMT')


timedata = ts(data$temperature,start=c(2018,8),frequency = 24)

plot(decompose(timedata))

library(xts)
library(forecast)

plot(decompose(timedata))

# Create train and test data
train <- window(timedata,end=c(2043,1))
test <- window(timedata,start=c(2043,2))

fitets <- ets(train,model="ZAA")
fcastets <- forecast(fitets, h = 21)
summary(fitets)

fitses <- ses(train,h=21)
fcastses <- forecast(fitses, h = 21)
summary(fitses)

accuracy(fcastets,test)
accuracy(fcastses,test)

plot(fcastets)
plot(fcastses)

plot(forecast(train,h=21))
plot(timedata)
