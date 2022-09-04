import progressHmstr as pg
import time

"""Example of use:"""
bar = pg.Bar(msg="Getting started:",
          symbol="#",
          empty_symbol="-",
          max_value=100,
          bar_format_symbol="`")
print(f"""{bar.get(msg="Getting ready:", action="Taking all cups out")}""")
time.sleep(5)
for i in range(1, 11):
    print(
        f"""{bar.update(msg="Making coffee:", action="Adding coffee")}""")
    time.sleep(0.2)
time.sleep(2)
for i in range(11, 26):
    print(f"""{bar.update(msg="Making coffee:", action="Adding water")}""")
    time.sleep(0.2)
time.sleep(2)
for i in range(26, 61):
    print(
        f"""{bar.update(msg="Making coffee:", action="Boiling coffee")}""")
    time.sleep(0.5)
time.sleep(2)
for i in range(61, 71):
    print(f"""{bar.update(msg="Making coffee:", action="Warming milk")}""")
    time.sleep(0.3)
time.sleep(2)
for i in range(71, 81):
    print(
        f"""{bar.update(msg="Making coffee:", action="Whipping milk")}""")
    time.sleep(0.5)
time.sleep(2)
for i in range(81, 86):
    print(
        f"""{bar.update(msg="Making coffee:", action="Adding coffee to cup")}"""
    )
    time.sleep(0.2)
time.sleep(2)
for i in range(86, 91):
    print(
        f"""{bar.update(msg="Making coffee:", action="Adding milk to coffee")}"""
    )
    time.sleep(0.2)
time.sleep(2)
for i in range(91, 96):
    print(
        f"""{bar.update(msg="Making coffee:", action="Waiting for coffee to cool")}"""
    )
    time.sleep(0.5)
time.sleep(2)
for i in range(96, 101):
    print(
        f"""{bar.update(msg="Making coffee:", action="Waiting for something to happen...?")}"""
    )
    time.sleep(0.2)
time.sleep(2)
print(bar.get())
print("Your coffee is ready")
