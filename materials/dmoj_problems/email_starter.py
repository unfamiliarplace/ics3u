# Email
# https://dmoj.ca/problem/ecoo19r2p1
# Stub

def sanitize_email(email: str) -> str:
    """
    Return a sanitized version of the given email address.
    
    Sanitization means:
    - Lowercase the email.
    - Remove any dots before the @ sign.
    - If there is a + followed by any sequence before the @ sign,
      the + and following sequence should be removed.
      
    >>> sanitize_email('foo@bar.com')
    'foo@bar.com'
    >>> sanitize_email('fO.o+baz123@bAR.com')
    'foo@bar.com'
    """
    # TODO Write this function

# There are 10 datasets, meaning the whole program should be wrapped in range(10)
for _ in range(10):
    n_emails = int(input())
    emails = set()
    
    for _ in range(n_emails):
        # TODO Get email input
        # TODO Sanitize the email
        # TODO Add it to the set

    print(len(emails))
