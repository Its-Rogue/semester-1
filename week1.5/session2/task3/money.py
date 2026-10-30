# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """
    
    
    
    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if valid_check(pounds, pence):
            self.pounds = pounds
            self.pence = pence
        else:
            raise TypeError("Invalid inputs")
        

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

        pad = ""
        if self.pence < 10:
            pad = "0"

        return (f"£{self.pounds}.{pad}{self.pence}")

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other, Money):
            raise TypeError("Input needs to be Type: Money")

        sum = [0,0]

        sum[0] = self.pounds + other.pounds
        sum[1] = self.pence + other.pence

        return Money(sum[0], sum[1])
    


def valid_check(pounds, pence):
        if not isinstance(pounds, int):
            return False

        if not pounds >= 0:
            return False

        if not isinstance(pence, int):
            return False

        if not pence >= 0 or not pence <= 99:
            return False

        return True