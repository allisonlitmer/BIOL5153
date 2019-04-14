
# coding: utf-8

# In[1]:

#CH. 5 exercise 1


# In[19]:

#write a function to tell what percent of aa is in the protein

def content(protein, aa):
    protein = protein.upper()
    aa = aa.upper()
    count_aa = protein.count(aa)
    length_p = len(protein)
    aa_content = count_aa * 100 / length_p
    return aa_content


  
    


# In[20]:

#run it

assert content("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert content("MSRSLLLRFLLFLLLLPPLP", "r") == 10 
assert content("MSRSLLLRFLLFLLLLPPLP", "L") == 50 
assert content("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


# In[21]:

#exercise 2


# In[37]:

#modify from part one to accept list of amino acid residues

#need a loop since list

def content(protein, aa = ['A', "I", "L", "M", "F", "W", "Y", "V"]):
    protein = protein.upper()
    length_p = len(protein)
    total = 0
    for aa_seq in aa:
        aa_seq = aa_seq.upper()
        count_aa = protein.count(aa_seq)
        total = total + count_aa
    aa_content = total * 100 / length_p
    return aa_content


# In[38]:

#test it

assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M']) == 5 
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55 
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70 
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65


# In[ ]:



