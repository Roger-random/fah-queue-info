#! /usr/bin/python3
'''
Telnet into localhost Folding@Home client and dump queue info
'''
import pprint
import telnetlib

WELCOMETEXT=b'\x1b[H\x1b[2JWelcome to the Folding@home Client command server.\n>'
TIMEOUT=1 # in seconds
QI_RESPONSE_START=b" \nPyON 1 units\n"
QI_RESPONSE_END=b"\n---\n> "

with telnetlib.Telnet("localhost",36330) as fah:
    # Read welcome prompt
    welcome = fah.read_until(b">",TIMEOUT)

    if welcome == WELCOMETEXT:
        # Request queue info and quit telnet.
        fah.write(b"queue-info\n")
        raw = fah.read_until(b"\n---\n> ",TIMEOUT)
        fah.write(b"quit\n")
        fah.close()

        # Process response
        if raw.startswith(QI_RESPONSE_START) and raw.endswith(QI_RESPONSE_END):
            # Trim off the start and end of response
            start_index = len(QI_RESPONSE_START)
            end_index = raw.rfind(QI_RESPONSE_END)
            trimmed = raw[slice(start_index,end_index)]

            if len(trimmed) > 0:
                # Evaluate the trimmed text.
                # NOTE: eval() is potentially dangerous if used with arbitrary data.
                # OK here because we (1) trust data from Folding@Home if it has
                # at least the expected start/end, and (2) we are only evaluating it
                # for pretty printing purposes.
                queueinfo = eval(trimmed)

                pp = pprint.PrettyPrinter(indent=2)
                pp.pprint(queueinfo)
        else:
            print("Did not see expected response to queue-info.")
            print("Actual response:")
            print(raw)
    else:
        # That's not the welcome prompt we expected...
        print("Did not see expected welcome prompt, aborting")
        print("Actual prompt seen:")
        print(welcome)