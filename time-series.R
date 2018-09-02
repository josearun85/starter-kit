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
