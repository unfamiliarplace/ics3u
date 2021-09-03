# Email
# https://dmoj.ca/problem/ecoo19r2p1
# Solution B (using split)

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
    email = email.lower()

    # Split it at the @ sign
    parts = email.split('@')
    pre_at = parts[0]
    post_at = parts[1]

    # As long as a '.' remains, remove it
    while '.' in pre_at:
        pre_at = pre_at.replace('.', '')

    # Split it at the plus. In this case we don't care what might be after it
    parts = pre_at.split('+')
    pre_plus = parts[0]
    
    # Splice it back together
    email = pre_plus + '@' + post_at
    
    return email

# There are 10 datasets, meaning the whole program should be wrapped in range(10)
for _ in range(10):
    n_emails = int(input())
    emails = set()
    
    for _ in range(n_emails):
        email = input()
        email = sanitize_email(email)
        emails.add(email)
        
    print(len(emails))
