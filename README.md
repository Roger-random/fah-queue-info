# Print Folding@Home Queue Info

Short Python 3 script to telnet into local F@H client and dump `queue-info`

[Linux installations for Folding@Home](https://foldingathome.org/alternative-downloads/) composes of three parts:
1. client - the part that performs the actual number-crunching
2. control - user interface to control client activity and see progress
3. viewer - fancy visual representation of work in progress

I usually don't care about #3, as it spends computing cycles that could go
towards folding.

My Windows clients come with a #2 equivalent control UI, where  I occasionally
need to pause folding in order to run other things. But when I have a Linux
client dedicated to F@H, they're set up to go full out and I rarely need to
change any behavior settings.

However, I would like to take a quick peek at their progress. For reasons not
important right now, I can't open up the Telnet port 36330 available on
F@H clients. This is my alternative: I can SSH into the machine and run this
Python 3 script to see the current client's queue information.