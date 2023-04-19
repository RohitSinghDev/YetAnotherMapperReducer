# YetAnotherMapperReducer
Mapper and Reducer Architecture and working replication using Socket programming

## Description
A project that replicates the mapper-reducer process of the Hadoop file system using socket programming in Python would involve implementing a distributed system 
that allows multiple nodes to work together to process large amounts of data.
The system would involve a central "master" node that coordinates the overall process and a set of "worker" nodes that perform the actual 
computation. The master node would be responsible for splitting up the input data into smaller chunks and assigning them to the worker nodes, 
as well as collecting the results from the workers and combining them to produce the final output.
The client file can be run in multiple devices and server file should be run in anyone 1 device. The mapper and reducer files are then transfered from server to client 
where further processsing takes place.
