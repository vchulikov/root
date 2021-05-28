#DS TO ASCII

import ostap.io.zipshelve as zs

db_file = zs.open("dataset.ds", 'c')
ds = db_file["ds_k"]
ds.write("dataset.txt")
ds.Print()
