def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return None
print(get_lead_ind([0,0,3]))
