# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import time

parcels = [
1,
2
]

expire = [
6221007025894,
6221007025917,
6221007032731,
6221025008237,
6221025032232,
6221042302011,
6221043030371,
6221075010037,
6221076010029,
6221077080311,
6221094088901,
6221508150613,
6222001407808,
6223002630011,
6223002642267,
6223003570682,
6223003931261,
6223003960568,
6223003970123,
6223003990510,
6223003990541,
6224000219703,
6224000437343,
6224001085994,
7613032321338,
7613034759344,
7613035477483,
7613035528970,
7613036199803,
]

invoices = [
2022100018260
]

##for x in expire:
    #time.sleep(3)
    ##subprocess.call(
       ## "adb shell am broadcast -a ACTION.SCAN.BARCODE -e com.symbol.datawedge.data_string" + " " + str(x) + " " + "-e com.symbol.datawedge.source scanner -e com.symbol.datawedge.label_type EAN13",
       ## shell=True)

for x in parcels:
    #time.sleep(1)
    subprocess.call(
        "adb shell am broadcast -a ACTION.SCAN.BARCODE -e com.symbol.datawedge.data_string" + " " + str(x) + " " + "-e com.symbol.datawedge.source scanner -e com.symbol.datawedge.label_type EAN13",
        shell=True)
