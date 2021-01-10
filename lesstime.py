def lesstime(start,end,dateofEvent):
    date = int(dateofEvent[0:4])
    return(start <= date <= end)
