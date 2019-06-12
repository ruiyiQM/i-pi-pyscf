import sys
sys.path.append("../../../")
from driver import RHFDriver, ExitSignal, TimeOutSignal

driver = RHFDriver(31415, "127.0.0.1", "template.gjf",["O", "H","H","O","H","H"],'sto-3g')
while True:
    try:
        driver.parse()
    except ExitSignal as e:
        driver = RHFDriver(31415, "127.0.0.1", "template.gjf", ["O", "H","H","O","H","H"],'sto-3g')
    except TimeOutSignal as e:
        print("Time out. Check whether the server is closed.")
        exit()
