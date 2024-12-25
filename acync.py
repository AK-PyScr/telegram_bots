import asyncio
import tkinter


class Window:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry('100x100')

        self.button = tkinter.Button(text="click", command=self.on_click).pack()

    def on_click(self):
        print("Button clicked!")

    async def async_tkinter_mainloop(self):
        while True:
            self.win.update()
            await asyncio.sleep(0.01)


    async def main(self):
        asyncio.create_task(self.async_tkinter_mainloop())
        num = await asyncio.to_thread(input, 'enter text ')
        print(num)


mainwindow = Window()

asyncio.run(mainwindow.main())
