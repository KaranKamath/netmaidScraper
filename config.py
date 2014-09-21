start_maid_id = 281772
end_maid_id = 300000

#This will disregard start and end parameters and only scrape what is already in the db
only_verify_existing = True

#Edit delays with caution
#Delays after successful scrapes
fixed_delay = 3
offset = 2 #should be < fixed_delay

#Delays after unsuccessful scrapes (404, for example)
fail_delay = 2
fail_offset = 1 #should be < fail_delay
