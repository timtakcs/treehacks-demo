This project should be a pub - sub system, with the publisher owned by Muzart and the subcribers owned by Tony, Batyr, and Timur.

The publisher sends weather data at some interval to the subscribers through a really simple message queue. 

The message queue is just a class that has a publish method and assign listener. Then it just calls all of its listeners in order.

The first subscriber pulls out the temperature and calculates the mean temperature.

The second publisher pulls out the temperature and date and maintains a key value map of the days and their temperatures in MM-DD-YY format.

The third publisher pulls out the precipitation data and keeps track of it in an array.