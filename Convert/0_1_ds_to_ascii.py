#FIRST PART
#DS TO ASCII
#REQUIREMENTS: *.DS FROM GANGA (Xic_2012_8Tev_MagUp.ds)

import ostap.io.zipshelve as zs

db_file = zs.open("Xic_2012_8Tev_MagUp.ds", 'c')
ds = db_file["ds_ksi2470"]
ds.write("Xic_2012_8Tev_MagUp_ds_ksi2470.txt")
ds.Print()
