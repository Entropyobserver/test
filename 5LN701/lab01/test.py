import re

# Refined regex pattern
#pattern = "\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)|(\w+\.(\w|\.)*)"
#pattern = r"(\w+\.(\w|\.)*)"
#pattern = r"(?:\d+\.\d+)|(?:\w\.(?:\w\.)+)|(?:\w+(?:-\w+)*)|[%#$“”.,:;!?‘’]"
#pattern = r"(?:\d+\.\d+)|\w+(?:-\w+)*|(?:[%#$]|(?:“|”|[.,:;!?‘’]))|(?:\b\w+'t\b)"
#pattern = "(?:\d+\.\d+)|(?:\w\.(?:\w\.)+)|\w+(?:-\w+)*|(?:\b\w+'t\b)|[%#$“”.,:;!?‘’]"
#pattern = r"(?:\d+\.\d+)|(?:\w\.(?:\w\.)+)|(?:\w+(?:-\w+)*)|(?:\b\w+'t\b)|[%#$“”.,:;!?‘’]"
#pattern = r"(?:\w+\.(?:\w+\.)+|\d+\.\d+|\w+(?:-\w+)*|\b\w+\'t\b|[%#$“”.,:;!?‘’])"
#pattern = r"(?:\w+\.(?:\w+\.)+|\d+\.\d+|\w+(?:-\w+)*|\b\w+'t\b|[%#$“”.,:;!?‘’])"
#pattern = "(?:\w+\.\w+(?:\.\w+)?|\d+\.\d+|\w+(?:-\w+)*|\b\w+'t\b|[%#$“”.,:;!?‘’])"
pattern = "(?:\w+\.\w+(?:\.\w+)*|\d+\.\d+|\w+(?:-\w+)*|\b\w+'t\b|[%#$“”.,:;!?‘’])"



# Test input
text = """
The 30-day simple yield fell to an average 8.19% from 8.22%; the
30-day compound yield slid to an average 8.53% from 8.56%. I am ready
at any instant to defy the Hanoverian brood--and I defy it now even
when face to face with the actual ruler of the enormous British
Empire!" Average maturity of the funds' investments lengthened by a
day to 41 days, the longest since early August. according to
Donoghue's. Sam is pursuing his Ph.D. And he picked up Lana
Clarkson, who was the hostess in the V.I.P. room, the Foundation Room,
it's called, at the House of Blues on Sunset Boulevard. The Treasury
said the U.S. will default on Nov. 9 if Congress doesn't act by then.
Pacific First Financial Corp. said shareholders approved its
acquisition by Royal Trustco Ltd. of Toronto for $27 a share, or $212
million. The House has voted to raise the ceiling to $3.1 trillion,
but the Senate isn't expected to act until next week at the earliest.
"""

# Tokenize using re.findall
tokens = re.findall(pattern, text)
print(tokens)