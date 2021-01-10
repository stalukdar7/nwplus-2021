def lessdist(lat_user,lon_user,lat_event,lon_event,radius):
    return (lat_user - lat_event <= radius) && (lon_user - lon_event <= radius)
