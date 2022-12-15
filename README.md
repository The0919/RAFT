## Jaron and Theo Awesome Sick-Nasty RAFT Thing

### Our High-level Approach

Our general approach to the project involved the iterative implementation of individual
components of RAFT. For example, first we created the backbone for a key-value store.
Then, we created handling for GETs. Then, PUTs. Then, elections, and so on.

We followed the RAFT documentation closely, basing our message structures off of their
counterparts. We made sure to break the code into functions for each handler and
action to make developing and debugging a smooth process.

### The Challenges We Faced

One of the challenges we faced was dealing with elections properly. We had to adjust
our timeouts so that elections would not happen too frequently and would have ample
time to complete before a replica started a new one.

Another challenge we faced was the implementation of the PUT command. There is some
complexity in maintaining the replica interactions involved. One conclusion we came to
was that handling only needed to occur in the handler for APPEND ACKs, so the leader
could forget about a particular APPEND until it received an ACK for it.

### A List of Properties/Features of Our Design That We Think Is Good

An interesting characteristic of the replicas in RAFT is the similarity to a state machine.
The different roles a replica assumes comes with different handling for messages. So, with
this in mind, we used a dictionary to organize our message handling, mapping from a STATE enum
(LEADER, CANDIDATE, FOLLOWER), to a nested map from MESSAGETYPE enum to a function(message: dict).

This kept our handling organized and encouraged the neat separation of functionality into
functions.

### An Overview of How We Tested Our Code

We tested our code with the automated tests, repeatedly running a test to analyze the results, then
investigating any unperformant statistics. We were able to diagnose issues in this manner.

