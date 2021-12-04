import r2pipe

r2 = r2pipe.open()
json = r2.cmdj('dptj')
for d in json:
    for key, value in d.items():
        if key == "pid":
            print("PID: " + str(value))
            command = "dpt= " + str(value)
            r2.cmd(command)
            print(r2.cmd("dbt"))

