import os, sys

if len(sys.argv) < 3:
    raise Exception("Please provide the path to the files! First - the reference, second - the one to be synced.")

fp_ref = sys.argv[1]
fp_sync = sys.argv[2]

ref_list = []
sync_list = []
new_list = []

with open(fp_ref, 'r') as file:
    ref_list = [line.rstrip() for line in file]
    #ref_list = file.readlines()

with open(fp_sync, 'r') as file:
    sync_list = [line.rstrip() for line in file]
    #sync_list = file.readlines()

new_list = [line for line in sync_list if line not in ref_list]

fp_new = fp_sync + ".edit"
with open(fp_new, 'w') as file:
    for line in new_list:
        file.write("%s\n" % line)
        #file.write(f"{line}\n")
