#20% of emails are spam, and 
#spam contains FREE in the body in 70% of the time. 
#Non-spam emails contain the word free 10% of the time. 
#Whats the probability that an email is spam if it contains the word FREEp


p_spam = 0.2
p_spam_free = 0.7
p_non_spam_free = 0.1   
p_non_spam = 1 - p_spam
p_free = (p_spam * p_spam_free) + (p_non_spam * p_non_spam_free)
p_spam_given_free = (p_spam * p_spam_free) / p_free
print(f"The probability that an email is spam given it contains the word 'FREE' is: {p_spam_given_free:.4f}")